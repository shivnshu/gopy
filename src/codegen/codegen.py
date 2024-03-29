#!/usr/bin/env python3
import sys
import os
import argparse

#sys.path.insert(0, os.environ['GoPyPATH'] + '/src/ir')
sys.path.insert(0, '../ir')
from ir_gen import ir_gen
from common import getCodeType, getLitType, free_all_regs
import assignments
import func_calls
import binaryop
import ifstmt
import gotostmt
import arr_decl
import struct_decl
import structs
import unaryop

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input", nargs="*")
args = arg_parser.parse_args()
input_file = open(args.input[0], "r")

ir_info = ir_gen(input_file)
#print(ir_info)
dict_code = ir_info['dict_code']
activation_records = ir_info['activationRecords']

context = {"last_func_call_ret": [], "func_ret": [], "rel_op_num": 0, "counter": 0, "array_decl": {}, "const_decl": {}, "float_vals": [],"float_stack": []}

def get_data_section(const_decl):
    global context
    res = []
    for line in const_decl:
        toks = line.split(" ", 2)
        lit_type = getLitType(toks[2])
        context["const_decl"][toks[0]] = lit_type
        res += [toks[0] + ": ." + lit_type + " " + toks[2]]
    return res

def asm_gen(code_line, func_name, scope, data_section):
    global context
    global activation_records
    activation_record = activation_records[scope]
    code_type = getCodeType(code_line)
    # print(code_line,code_type, "IN CODEGEN")
    #print("AAA:" + code_type)
    if (code_type == "assignments"):
        res, context = assignments.asm_gen(code_line, activation_record, context, data_section, activation_records)
        return res
    if (code_type == "function-call"):
        res, context = func_calls.asm_gen(code_line, activation_record, func_name, context, data_section, activation_records)
        return res
    if (code_type == "binary-op"):
        res, context = binaryop.asm_gen(code_line, activation_record, context, activation_records)
        return res
    if (code_type == "ifstmt"):
        res = ifstmt.asm_gen(code_line, context, activation_records)
        return res
    if (code_type == "gotostmt"):
        return gotostmt.asm_gen(code_line,activation_record, activation_records)
    if (code_type == "arr_decl"):
        res, context = arr_decl.asm_gen(code_line, activation_record, context, activation_records)
        return res
    # change getcodetype
    if (code_type == "struct_decl"):
        return struct_decl.asm_gen(code_line, activation_record, activation_records)
    if (code_type == "structs"):
        res, context = structs.asm_gen(code_line, activation_record, context, activation_records, data_section)
        return res
    if (code_type == "unary-op"):
        res, context = unaryop.asm_gen(code_line, activation_record, context, activation_records)
        return res
    return [code_line]

def alloc_st_code(func_name):
    act_record = activation_records[func_name]
    local_vars = act_record.getLocalVars()
    min_offset = 0
    for key in local_vars:
        (offset, size) = local_vars[key]
        min_offset = min(min_offset, offset)
    return ["subl $" + str(abs(min_offset)) + ", %esp"]

def main(dict_code):
    global activation_records
    data_section = [".section .data"]

    res = [".section .text", ".globl main", ""]
    res += ["main:", "push %ebp", "movl %esp, %ebp", "movl %ebp, %esi"]
    res += alloc_st_code("root")

    if 'global_decl' in dict_code:
        code_list = dict_code['global_decl'][0]
        scope_list = dict_code['global_decl'][1]
        for code_line, scope in zip(code_list, scope_list):
            gen_code = asm_gen(code_line, "root", scope, data_section)
            if (gen_code != None):
                res += gen_code
            else:
                print("Code generation error for line: ", code_line)

    res += ["call func_main", "push $0", "call exit", ""]
    func_init = ["push %ebp", "mov %esp, %ebp"]
    func_end = ["mov %ebp, %esp", "pop %ebp", "ret", ""]

    if 'const_decl' in dict_code:
        data_section += get_data_section(dict_code['const_decl'][0])

    for func_name in dict_code:
        free_all_regs() # Free if new function comes
        if (func_name == "global_decl" or func_name == "const_decl"):
            continue
        if (func_name == "main"):
            res += ["func_main:"]
        else:
            res += [func_name + ":"]
        res += func_init
        code_list = dict_code[func_name][0]
        scope_list = dict_code[func_name][1]
        res += alloc_st_code(func_name)
        ret_added = False
        for code_line, scope in zip(code_list, scope_list):
            gen_code = asm_gen(code_line, func_name, scope, data_section)
            if (code_line == "func_end"):
                res += func_end
                ret_added = True
            elif (gen_code != None):
                res += gen_code
                ret_added = False
            else:
                print("Code generation error for line: ", code_line)
        if not ret_added:
            res += func_end
    res += data_section
    return res

code_lines = main(dict_code)
print("+++++++++++++++++++++++++++++++++++++++++++++++++")
for code_line in code_lines:
    print(code_line)

output_file = "tmp.S"
if len(args.input) > 1:
    output_file = args.input[1] + ".S"
f = open(output_file, "w")
for code_line in code_lines:
    f.write(code_line + "\n")
