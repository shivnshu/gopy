import sys
from common import get_register, free_register, getTokType

size_of = {'int': '4', 'float': '4', 'char': '1', "*int": '4', "*float": '4', "*char": '4', "string": '4'}

def asm_gen(line, activation_record, context, activation_records):
    global size_of
    res = []
    toks = line.split()
    # print(toks)
    arr_var = toks[3]
    type_size = size_of[toks[2]]

    dimentions = []
    for i in range(4, len(toks)):
        d = toks[i]
        if getTokType(d) != "positive-integer":
            print("Error(arr_decl): only const indexes are allowed")
            sys.exit(0)
        dimentions += [d]

    context['array_decl'][toks[3]] = {"size": type_size, "dimentions": dimentions}

    (offset, jmp), typ = activation_record.getVarTuple(arr_var, activation_records)
    reg_ = get_register("_pqr")
    res += ["movl %ebp, " + reg_]
    while (jmp > 0):
        res += ["movl ("+reg_+"), " + reg_]
        jmp -= 1
    if (offset >= 0):
        return res, context # Variable is not local

    if typ == "global" or typ == "const":
        print("Error: unsupported code:", line)
        sys.exit(0)

    reg = get_register("_tmp")

    res += ["movl $" + toks[4] + ", " + reg]
    for i in range(5, len(toks)):
        res += ["imul $" + toks[i] + ", " + reg]
    res += ["imul $" + type_size + ", " + reg]
    res += ["push %eax"]
    res += ["push " + reg]
    res += ["call malloc"]
    res += ["movl %eax, " + str(offset) + "("+reg_+")"]
    res += ["pop %eax"]

    free_register("_tmp")
    free_register("_pqr")
    return res, context
