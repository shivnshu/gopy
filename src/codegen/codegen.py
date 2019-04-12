#!/usr/bin/env python3
import sys
import argparse

sys.path.insert(0, '../ir')
from ir_gen import ir_gen
from common import getCodeType
import assignments

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input", nargs="*")
args = arg_parser.parse_args()
input_file = open(args.input[0], "r")

ir_info = ir_gen(input_file)
#print(ir_info)
dict_code = ir_info['dict_code']
activation_records = ir_info['activationRecords']

def asm_gen(code_line, func_name):
    code_type = getCodeType(code_line)
    if (code_type == "assignments"):
        return assignments.asm_gen(code_line, activation_records[func_name])
    else:
        None


def main():
    res = [".section .text", ".globl main", ""]
    res += ["main:", "call _init", "call func_main", "push $0", "call exit", ""]
    res += ["_init:", "push %ebp", "movl %esp, %ebp", "movl %ebp, %esp", "pop %ebp", "ret", ""]
    func_init = ["push %ebp", "mov %esp, %ebp"]
    func_end = ["mov %ebp, %esp", "pop %ebp", "ret"]
    for func_name in dict_code:
        res += ["func_" + func_name + ":"]
        res += func_init
        code_list = dict_code[func_name]
        for code_line in code_list:
            res += asm_gen(code_line, func_name)
        res += func_end
    return res

code_lines = main()
for code_line in code_lines:
    print(code_line)
