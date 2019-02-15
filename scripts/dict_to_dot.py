#!/usr/bin/env python
from graphviz import Digraph

inp = {'label': 'Start', 'id': '3', 'children': [{'label': 'PackageClause', 'id': '2', 'children': [{'label': 'package', 'id': '0', 'children': []}, {'label': 'main', 'id': '1', 'children': []}]}]}
dot = Digraph()

def dict_to_dot(inp):
    global dot
    if 'id' not in inp:
        return
    dot.node(inp['id'], inp['label'])
    for child in inp['children']:
        if 'id' not in child:
            continue
        dot.edge(inp['id'], child['id'])
        dict_to_dot(child)

dict_to_dot(inp)

print(dot.source)

