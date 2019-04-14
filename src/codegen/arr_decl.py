import common
from common import get_register, free_register, getTokType

size_of = {'int': '4', 'float': '4', 'char': '1'}

def asm_gen(line, activation_record, context):
    global size_of
    res = []
    toks = line.split()
    # print(toks)
    arr_var = toks[3]
    type_size = size_of[toks[2]]

    (offset, size), typ = activation_record.getVarTuple(arr_var)
    dim_offset = offset + 4

    if typ != "global" and typ != "const":
        res += ["movl " + get_register(toks[4]) + ", " + str(dim_offset) + "(%ebp)"]
        dim_offset += 4  # Assumption: toks always register
        free_register(toks[4])
        for i in range(5, len(toks)):
            res += ["movl " + get_register(toks[i]) + ", " + str(dim_offset) + "(%ebp)"]
            free_register(toks[i])

        reg = get_register("_tmp")

        dim_offset = offset + 4
        res += ["movl " + str(dim_offset) + "(%ebp)" + ", " + reg]
        dim_offset += 4
        for i in range(5, len(toks)):
            res += ["imul " + str(dim_offset) + "(%ebp)" + ", " + reg]
        res += ["imul $" + type_size + ", " + reg]
        res += ["push %eax"]
        res += ["push " + reg]
        res += ["call malloc"]
        res += ["movl %eax, " + str(offset) + "(%ebp)"]
        res += ["pop %eax"]
        free_register("_tmp")
        context['array_decl'][toks[3]] = type_size
    return res, context
