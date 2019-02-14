#!/usr/bin/env python3
import argparse
from parser import go_parser

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--out", help="Output dot script")
arg_parser.add_argument("input", nargs="*")

args = arg_parser.parse_args()

input_file = open(args.input[0], "r")
output_file = args.out

input_data = input_file.read()

print(go_parser.parse(input_data))
