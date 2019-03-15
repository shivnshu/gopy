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
        # print(grammer_list)
        line = grammer_list[i]
    return (out, i)

output = ''
counter = 0

output += "import ply.yacc as yacc\n\n"
output += "from tokrules import tokens\n\n"
output += "from SymbolTable import SymbolTable\n"
# output += "from SymbolTable import SymbolTableLiteralEntry as LitEntry\n"
output += "from SymbolTable import SymbolTableVariableEntry as VarEntry\n"
output += "from SymbolTable import SymbolTablePackageEntry as PackageEntry\n"
output += "from SymbolTable import SymbolTableInterfaceEntry as InterfaceEntry\n"
output += "from SymbolTable import SymbolTableStructEntry as StructEntry\n"
output += "from SymbolTable import SymbolTableFunctionEntry as FuncEntry\n"
output += "from SymbolTable import SymbolTableImportEntry as ImportEntry\n\n"

output += "symTableDict = {'rootSymTable': SymbolTable(None, 'rootSymTable')}\n"
output += "symTableSt = ['rootSymTable']\n"

output += "counter = 0\n"
output += "label_counter = 0\n\n"

output += "def newVar():\n"
output += "\tglobal counter\n"
output += "\tres = 't' + str(counter)\n"
output += "\tcounter += 1\n"
output += "\treturn res\n\n"

output += "def newLabel():\n"
output += "\tglobal label_counter\n"
output += "\tres = 'label' + str(counter)\n"
output += "\tlabel_counter += 1\n"
output += "\treturn res\n\n"

output += "def verifyCalType(name, lineno):\n"
output += "\tflag = False\n"
output += "\tfor n in symTableSt[::-1]:\n"
output += "\t\tif name in symTableDict[n].symbols:\n"
output += "\t\t\tflag = True\n"
output += "\t\t\ttable = symTableDict[n]\n"
output += "\t\t\tbreak\n"
output += "\tif not flag:\n"
output += "\t\tprint('Type of', name, 'not found on line number', lineno)\n"
output += "\t\treturn 'Unknown'\n"
output += "\tentry = table.get(name)\n"
output += "\treturn entry.getType()\n\n"

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
    output += "\tglobal symTableSt\n\tglobal symTableDict\n"
    output += "\tp[0] = {}\n"
    output += "\tp[0]['code'] = []\n"
    output += tmp_out
    if (len(tmp_out) == 0):
        i -= 1

    for prod_i in range(num_productions):
        line = grammer_list[prod_i]
        prod_elems = line.split()
        prod_len = len(prod_elems)
        if (prod_i == 0):
            prod_len -= 1
        (tmp_out, i) = insertActionsHelper(prod_i+1, grammer_list, i+1, 2)
        if (tmp_out == ""):
            i -= 1
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
