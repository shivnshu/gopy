import sys
from common import get_register, free_register, getTokType, reserve_register, unreserve_register

size_of = {'int': '4', 'float': '4', 'char': '1', "*int": '4', "*float": '4', "*char": '4', "string": '4'}
lang_datatypes = ["int", "float", "bool"]

def asm_gen(line, activation_record, activation_records):
    res = []
    toks = line.split()
    struct_type = toks[1]
    if (struct_type in lang_datatypes):
        return res
    var_name = toks[2]
    (offset, size), typ = activation_record.getVarTuple(var_name, activation_records)
    if (typ == "global" or typ == "const"):
        print("Error: unsupported", typ, "for", var_name)
        sys.exit(0)
    var_sign = activation_record.getSign(var_name)
    var_size = 0
    for field in var_sign:
        tupl = var_sign[field]
        var_size = max(var_size, tupl[0]+tupl[1])
    reserve_register("%eax")
    res += ["subl $4, %esp"]
    res += ["push %eax"]
    res += ["push $" + str(var_size)]
    res += ["call malloc"]
    res += ["movl %eax, " + str(offset) + "(%ebp)"]
    res += ["pop %eax"]
    unreserve_register("%eax")
    return res

