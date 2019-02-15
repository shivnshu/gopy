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
output += "counter = 0\n"

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
    output += "\n\t'''\n"
    output += '\tglobal counter\n'
    if (is_terminal_production):
        output += '\tp[0] = {"label" : p[1], "id": str(counter)}\n'
    else:
        output += '\tp[0] = {"label": "' + clause_name + '", "id": str(counter)}\n'
    output += '\tcounter += 1\n'
    counter += 1
    # if (counter > 5):
    #     break
    if (len(children_lengths) == 1):
        if (is_terminal_production):
            output += "\tp[0]['children'] = []" + "\n"
        else:
            output += "\t" + children_helper(children_lengths[0]) + "\n"
        output += '\n'
        continue
    output += "\tif (len(p) == " + str(children_lengths[0]) + "):\n"
    output += "\t\t" + children_helper(children_lengths[0]) + "\n"

    for i in range(1, len(children_lengths)-1):
        output += "\telif (len(p) == " + str(children_lengths[i]) + "):\n"
        output += "\t\t" + children_helper(children_lengths[i]) + "\n"

    output += "\telse:\n"
    output += "\t\t" + children_helper(children_lengths[-1]) + "\n"
    output += "\n"

output += '''
def p_error(p):
\tprint("Error encountered at line number", p.lineno)

go_parser = yacc.yacc(start="SourceFile")
'''

print(output)
