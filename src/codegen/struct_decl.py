import sys
from common import get_register, free_register, getTokType, reserve_register, unreserve_register

size_of = {'int': '4', 'float': '4', 'char': '1', "*int": '4', "*float": '4', "*char": '4', "string": '4'}
lang_datatypes = ["int", "float", "bool", "*int", "*float", "string", "*bool"]

def asm_gen(line, activation_record, activation_records):
    res = []
    toks = line.split()
    struct_type = toks[1]
    if (struct_type in lang_datatypes):
        return res
    var_name = toks[2]
    (offset, jmp), typ = activation_record.getVarTuple(var_name, activation_records)
    reg_ = get_register("_pqr")
    res += ["movl %ebp, " + reg_]
    while (jmp > 0):
        res += ["movl ("+reg_+"), " + reg_]
        jmp -= 1
    if (typ == "global" or typ == "const"):
        print("Error: unsupported", typ, "for", var_name)
        sys.exit(0)
    var_sign = activation_record.getSign(var_name)
    var_size = 0
    for field in var_sign:
        tupl = var_sign[field]
        var_size = max(var_size, tupl[0]+tupl[1])
    reserve_register("%eax")
    res += ["push %eax"]
    res += ["push $" + str(var_size)]
    res += ["call malloc"]
    res += ["movl %eax, " + str(offset) + "("+reg_+")"]
    res += ["pop %eax"]
    free_register("_pqr")
    unreserve_register("%eax")
    return res

