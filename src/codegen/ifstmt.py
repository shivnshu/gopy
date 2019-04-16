import common
from common import get_register, free_register, getTokType

def asm_gen(line, context, activation_records):
    res = []
    toks = line.split()

    '''
    Some niggas like pow are left out
    '''

    l1 = toks[3]
    if toks[1] in context["float_stack"]:
        res += ["fld1"]
        res += ["fcomip"]
        res += ["fstp %st(0)"]
        res += ["je " + l1]
    else:
        r = get_register(toks[1])
        res.append("cmpl $1, " + r)
        res.append("je " + l1)
        free_register(toks[1])

    if (len(toks) == 7):
        l2 = toks[6]
        res.append("jmp " + l2)


    return res
