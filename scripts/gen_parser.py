#!/usr/bin/env python3
import sys
import re

if (len(sys.argv) < 2):
    print("Usage: ./bin grammer")
    sys.exit(0)

def camelToSnake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def children_helper(length):
    res = "p[0]['children'] = ["
    for i in range(1, length-1):
        res += "p[" + str(i) + "], "
    res += "p[" + str(length-1) + "]]"
    return res

output = ''
counter = 0

output += "import ply.yacc as yacc\n\n"
output += "from tokrules import tokens\n\n"
output += "from SymbolTable import SymbolTable\n"
output += "from SymbolTable import SymbolTableLiteralEntry as LiteralEntry\n"
output += "from SymbolTable import SymbolTableVariableEntry as VariableEntry\n"
output += "from SymbolTable import SymbolTableFunctionEntry as FunctionEntry\n\n"
output += "symTableDict = {'rootSymTable': SymbolTable(None, 'rootSymTable')}\n"
output += "symTableSt = ['rootSymTable']\n\n"


output += '''
def p_empty(p):
\t'empty :'
\tpass\n
'''

data = open(sys.argv[1], "r").read()

grammers = data.split('\n\n')

for grammer in grammers:
    words = grammer.split()
    if (len(words) == 0):
        continue
    clause_name = words[0]
    children_lengths = []
    is_terminal_production = False
    cfg = grammer
    for line in cfg.split('\n'):
        tokens = line.split()
        if (len(tokens) == 0):
            continue
        is_terminal_production = tokens[-1].isupper()
        children_lengths.append(len(tokens))
    children_lengths[0] -= 1

    is_terminal_production &= (len(children_lengths) == 1)

    output += 'def p_' + camelToSnake(clause_name) + '(p):\n'
    output += "\t'''\n"
    for line in cfg.split('\n'):
        output += "\t" + line + "\n"
    output = output[:-1]
    output += "\n\t'''\n\n"

output += '''
def p_error(p):
\tprint("Error encountered at line number", p.lineno)

go_parser = yacc.yacc(start="SourceFile", write_tables=False)
'''

print(output)
