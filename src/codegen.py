#!/usr/bin/env python3

import argparse
from parser_tmp import go_parser

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input", nargs="*")
args = arg_parser.parse_args()

input_file = open(args.input[0], "r")

input_data = input_file.read()
result = go_parser.parse(input_data)

print(result)
