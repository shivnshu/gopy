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

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input", nargs="*")
args = arg_parser.parse_args()
input_file = open(args.input[0], "r")

ir_info = ir_gen(input_file)
#print(ir_info)
dict_code = ir_info['dict_code']
activation_records = ir_info['activationRecords']

context = {"last_func_call_ret": [], "func_ret": [], "rel_op_num": 0}

def get_data_section(const_decl):
    res = [".section .data"]
    for line in const_decl:
        toks = line.split(" ", 2)
        lit_type = getLitType(toks[2])
        res += [toks[0] + ": ." + lit_type + " " + toks[2]]
    return res

def asm_gen(code_line, func_name):
    global context
    code_type = getCodeType(code_line)
    if (code_type == "assignments"):
        res, context = assignments.asm_gen(code_line, activation_records[func_name], context)
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
    return None
    # return [code_line]

def alloc_st_code(func_name):
    act_record = activation_records[func_name]
    local_vars = act_record.getLocalVars()
    min_offset = 0
    for key in local_vars:
        (offset, size) = local_vars[key]
        min_offset = min(min_offset, offset)
    return ["subl $" + str(abs(min_offset)) + ", %esp"]

def main():
    res = [".section .text", ".globl main", ""]
    res += ["main:", "call _init", "call func_main", "push $0", "call exit", ""]
    res += ["_init:", "push %ebp", "movl %esp, %ebp", "movl %ebp, %esp", "pop %ebp", "ret", ""]
    func_init = ["push %ebp", "mov %esp, %ebp"]
    func_end = ["mov %ebp, %esp", "pop %ebp", "ret", ""]
    for func_name in dict_code:
        free_all_regs() # Free if new function comes
        if (func_name == "global_decl" or func_name == "const_decl"):
            continue
        if (func_name == "main"):
            res += ["func_main:"]
        else:
            res += [func_name + ":"]
        res += func_init
        res += alloc_st_code(func_name)
        code_list = dict_code[func_name]
        for code_line in code_list:
            if (code_line == "call fmt.Printf"):
                code_line = "call printf"
            gen_code = asm_gen(code_line, func_name)
            if (gen_code != None):
                res += gen_code
            else:
                print("Code generation error for line: ", code_line)
        res += func_end
    if 'const_decl' in dict_code:
        res += get_data_section(dict_code['const_decl'])
    return res

code_lines = main()
print("+++++++++++++++++++++++++++++++++++++++++++++++++")
for code_line in code_lines:
    print(code_line)
f = open("tmp.S", "w")
for code_line in code_lines:
    f.write(code_line + "\n")
