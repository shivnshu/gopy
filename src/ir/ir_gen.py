#!/usr/bin/env python3

import argparse
from parser import go_parser

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input", nargs="*")
args = arg_parser.parse_args()
input_file = open(args.input[0], "r")

def ir_gen(input_file):
    input_data = input_file.read()
    result = go_parser.parse(input_data)
    return result

#ir_gen(input_file)
