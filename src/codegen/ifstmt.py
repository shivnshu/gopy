import common
from common import get_register, free_register, getTokType

def asm_gen(line, activation_records):
    res = []
    toks = line.split()

    '''
    Some niggas like pow are left out
    '''

    r = get_register(toks[1])
    l1 = toks[3]
    res.append("cmpl $1, " + r)
    res.append("je " + l1)
    if (len(toks) == 7):
        l2 = toks[6]
        res.append("jmp " + l2)

    free_register(toks[1])

    return res
