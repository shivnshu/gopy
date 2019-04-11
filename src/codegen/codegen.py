#!/usr/bin/env python3
import sys
import argparse

sys.path.insert(0, '../ir')
from ir_gen import ir_gen

import assignments

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input", nargs="*")
args = arg_parser.parse_args()
input_file = open(args.input[0], "r")

ir_info = ir_gen(input_file)
#print(ir_info)
dict_code = ir_info['dict_code']
activation_records = ir_info['activationRecords']

def asm_gen(line):
    # Detect line type
    print(assignments.asm_gen(line, activation_records[func_name]))

for func_name in dict_code:
    code = dict_code[func_name]
    for line in code:
        asm_gen(line)
