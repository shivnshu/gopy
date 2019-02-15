#!/usr/bin/env python3
import argparse
import sys
from graphviz import Digraph
from parser import go_parser

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--out", help="Output dot script")
arg_parser.add_argument("input", nargs="*")
args = arg_parser.parse_args()

dot = Digraph()

def dict_to_dot(inp):
    global dot
    if 'id' not in inp:
        return
    dot.node(inp['id'], inp['label'])
    for child in inp['children']:
        if child == None:
            continue
        if 'id' not in child:
            continue
        dot.edge(inp['id'], child['id'])
        dict_to_dot(child)

if (len(args.input) == 0):
    print("Please specify input code")
    sys.exit(0)

input_file = open(args.input[0], "r")

input_data = input_file.read()
dict_result = go_parser.parse(input_data)

print(dict_result)

if (args.out == None):
    sys.exit(0)

output_file = args.out
output_handler = open(output_file, "w")

dict_to_dot(dict_result)

output_handler.write(dot.source)
output_handler.close()
print(dot.source)
