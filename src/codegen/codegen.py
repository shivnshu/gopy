#!/usr/bin/env python3
import sys
import argparse

sys.path.insert(0, '../ir')
from ir_gen import ir_gen
from common import getCodeType, getLitType, free_all_regs
import assignments
import func_calls
import binaryop
import ifstmt
import gotostmt
import arr_decl
import structs

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input", nargs="*")
args = arg_parser.parse_args()
input_file = open(args.input[0], "r")

ir_info = ir_gen(input_file)
#print(ir_info)
dict_code = ir_info['dict_code']
activation_records = ir_info['activationRecords']

context = {"last_func_call_ret": [], "func_ret": [], "rel_op_num": 0, "counter": 0, "array_decl": {}, "const_decl": {}}

def get_data_section(const_decl):
    global context
    res = []
    for line in const_decl:
        toks = line.split(" ", 2)
        lit_type = getLitType(toks[2])
        context["const_decl"][toks[0]] = lit_type
        res += [toks[0] + ": ." + lit_type + " " + toks[2]]
    return res

def asm_gen(code_line, func_name, data_section):
    global context
    code_type = getCodeType(code_line)
    if (code_type == "assignments"):
        res, context = assignments.asm_gen(code_line, activation_records[func_name], context, data_section)
        return res
    if (code_type == "function-call"):
        res, context = func_calls.asm_gen(code_line, activation_records, func_name, context)
        return res
    if (code_type == "binary-op"):
        res, context = binaryop.asm_gen(code_line, activation_records[func_name], context)
        return res
    if (code_type == "ifstmt"):
        res = ifstmt.asm_gen(code_line, activation_records)
        return res
    if (code_type == "gotostmt"):
        return gotostmt.asm_gen(code_line)
    if (code_type == "arr_decl"):
        res, context = arr_decl.asm_gen(code_line, activation_records[func_name], context)
        return res
    if (code_type == "structs"):
        return structs.asm_gen(code_line, activation_records[func_name])
    # return None
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
    res = [".section .text", ".globl main", ""]
    res += ["main:", "push %ebp", "movl %esp, %ebp", "movl %ebp, %esi"]
    res += alloc_st_code("root")

    if 'global_decl' in dict_code:
        code_list = dict_code['global_decl']
        for code_line in code_list:
            gen_code = asm_gen(code_line, "root")
            if (gen_code != None):
                res += gen_code
            else:
                print("Code generation error for line: ", code_line)

    res += ["call func_main", "push $0", "call exit", ""]
    func_init = ["push %ebp", "mov %esp, %ebp"]
    func_end = ["mov %ebp, %esp", "pop %ebp", "ret", ""]
    data_section = [".section .data"]

    if 'const_decl' in dict_code:
        data_section += get_data_section(dict_code['const_decl'])

    for func_name in dict_code:
        free_all_regs() # Free if new function comes
        if (func_name == "global_decl" or func_name == "const_decl"):
            continue
        if (func_name == "main"):
            res += ["func_main:"]
        else:
            res += [func_name + ":"]
        res += func_init
        code_list = dict_code[func_name]
        res += alloc_st_code(func_name)
        for code_line in code_list:
            gen_code = asm_gen(code_line, func_name, data_section)
            if (gen_code != None):
                res += gen_code
            else:
                print("Code generation error for line: ", code_line)
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
