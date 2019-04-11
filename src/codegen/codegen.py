#!/usr/bin/env python3
import sys
import argparse

sys.path.insert(0, '../ir')

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input", nargs="*")
args = arg_parser.parse_args()
input_file = open(args.input[0], "r")

from ir_gen import ir_gen

ir_code = ir_gen(input_file)
print(ir_code['dict_code'])
