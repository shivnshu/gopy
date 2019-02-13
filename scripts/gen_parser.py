#!/usr/bin/env python3
import sys
import re

if (len(sys.argv) < 2):
    print("Usage: ./bin grammer")
    sys.exit(0)

output = ''
counter = 0

def camelToSnake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

data = open(sys.argv[1], "r").read()

grammers = data.split('\n\n')

for grammer in grammers:
    # print(grammer)
    words = grammer.split()
    clause_name = words[0]
    m = re.match(r"([\w\s:|\'=\*]*)<<([\w\n\s\[\]\'=\,]*)>>", grammer)
    cfg = m.group(1).strip()
    children = m.group(2).strip()
    output += 'def p_' + camelToSnake(clause_name) + '(p):\n'
    output += '\t'
    output += "'''\n\t" + cfg + "\n\t'''\n"
    output += '\tglobal counter\n'
    output += '\tp[0] = {"label": "' + clause_name + '", "id": str(counter)}\n'
    output += '\t' + children + '\n'
    output += '\tcounter += 1\n'
    output += '\n'
    counter += 1
    # if (counter > 89):
    #     break

print(output)
