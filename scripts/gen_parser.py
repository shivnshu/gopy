#!/usr/bin/env python3
import sys
import re

if (len(sys.argv) < 2):
    print("Usage: ./bin grammer")
    sys.exit(0)

def camelToSnake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def insertActionsHelper(prod_num, grammer_list, i, tabs_num):
    out = ""
    if (i >= len(grammer_list)):
        return (out, i)
    line = grammer_list[i]
    if (line != "<<" + str(prod_num)):
        return (out,i)
    i += 1
    line = grammer_list[i]
    while (line != ">>"):
        for j in range(tabs_num):
            out += "\t"
        out += line
        out += "\n"
        i += 1
        line = grammer_list[i]
    return (out, i)

output = ''
counter = 0

output += "import ply.yacc as yacc\n\n"
output += "from tokrules import tokens\n\n"
output += "from SymbolTable import SymbolTable\n"
output += "from SymbolTable import SymbolTableLiteralEntry as LiteralEntry\n"
output += "from SymbolTable import SymbolTableVariableEntry as VariableEntry\n"
output += "from SymbolTable import SymbolTableFunctionEntry as FunctionEntry\n\n"
output += "symTableDict = {'rootSymTable': SymbolTable(None, 'rootSymTable')}\n"
output += "symTableSt = ['rootSymTable']\n"

output += '''
def p_empty(p):
\t'empty :'
\tpass\n
'''

data = open(sys.argv[1], "r").read()

grammers = data.split('\n\n')

for grammer in grammers:
    words = grammer.split()
    num_productions = 0
    if (len(words) == 0):
        continue
    clause_name = words[0]
    output += 'def p_' + camelToSnake(clause_name) + '(p):\n'
    output += "\t'''\n"
    i = 0
    grammer_list = grammer.split('\n')

    for i in range(len(grammer_list)):
        line = grammer_list[i]
        if (line[:2] == "<<"):
            break
        output += "\t" + line + "\n"
        num_productions += 1
    output = output[:-1]
    output += "\n\t'''\n"
    (tmp_out, i) = insertActionsHelper(0, grammer_list, i, 1)
    output += tmp_out

    for prod_i in range(num_productions):
        line = grammer_list[prod_i]
        prod_elems = line.split()
        prod_len = len(prod_elems)
        if (prod_i == 0):
            prod_len -= 1
        (tmp_out, i) = insertActionsHelper(prod_i+1, grammer_list, i+1, 2)
        if (tmp_out == ""):
            continue
        output += "\t" + "if len(p)==" + str(prod_len)
        for j in range(-1, -1*prod_len, -1):
            output += " and "
            output += "p.slice[" + str(prod_len+j) + "].type=="
            output += '"' + prod_elems[j] + '"'
        output += ":\n"
        output += tmp_out

    output += "\n"


output += '''
def p_error(p):
\tprint("Error encountered at line number", p.lineno)

go_parser = yacc.yacc(start="SourceFile", write_tables=False)
'''

print(output)
