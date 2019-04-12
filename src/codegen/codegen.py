#!/usr/bin/env python3
import sys
import argparse

sys.path.insert(0, '../ir')
from ir_gen import ir_gen
from common import getCodeType
import assignments
import func_calls

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input", nargs="*")
args = arg_parser.parse_args()
input_file = open(args.input[0], "r")

ir_info = ir_gen(input_file)
#print(ir_info)
dict_code = ir_info['dict_code']
activation_records = ir_info['activationRecords']

context = {"last_func_call_ret": [], "last_func_call_ret_offset": 0, "func_ret": []}

def asm_gen(code_line, func_name):
    global context
    code_type = getCodeType(code_line)
    if (code_type == "assignments"):
        return assignments.asm_gen(code_line, activation_records[func_name])
    if (code_type == "function-call"):
        res, context = func_calls.asm_gen(code_line, activation_records, func_name, context)
        return res
    return None

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
        if (func_name == "global_decl"):
            continue
        if (func_name == "main"):
            res += ["func_main:"]
        else:
            res += [func_name + ":"]
        res += func_init
        res += alloc_st_code(func_name)
        code_list = dict_code[func_name]
        for code_line in code_list:
            gen_code = asm_gen(code_line, func_name)
            if (gen_code != None):
                res += gen_code
        res += func_end
    return res

code_lines = main()
print("+++++++++++++++++++++++++++++++++++++++++++++++++")
for code_line in code_lines:
    print(code_line)
