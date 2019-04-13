import common
from common import get_register, free_register, getTokType

sizes = {'int': 4, 'float': 4, 'char': 1}

def asm_gen(line, context):
    res = []
    toks = line.split()
    type_size = sizes[toks[2]]

    return res
