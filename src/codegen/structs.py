import sys
from common import get_register, free_register, getTokType

size_of = {'int': '4', 'float': '4', 'char': '1', "*int": '4', "*float": '4', "*char": '4', "string": '4'}

def asm_gen(line, activation_record):
    res = []
    toks = line.split()
    if ("." in toks[0]):
        var_field = toks[0].split(".")
        var_name = var_field[0]
        field_name = var_field[1]
        assert(getTokType(var_name) == "variable")
        (offset, size), typ = activation_record.getVarTuple(var_name)
        if (typ == "global" or typ == "const"):
            print("Error: unsupported type", type, "of", var_name)
            sys.exit(0)
        (field_offset, size, typ) = activation_record.getSign(var_name)[field_name]
        # Assuming right type to be a register
        reg_name = toks[-1]
        res += ["movl " + get_register(reg_name) + ", " + str(offset+field_offset) + "(%ebp)"]
        return res

    # Struct is on right side
    var_field = toks[2].split(".")
    var_name = var_field[0]
    field_name = var_field[1]
    left_param = toks[0]
    left_type = getTokType(left_param)
    assert(getTokType(var_name) == "variable")
    (offset, size), typ = activation_record.getVarTuple(var_name)
    if (typ == "global" or typ == "const"):
        print("Error: unsupported type", type, "of", var_name)
        sys.exit(0)
    (field_offset, size, typ) = activation_record.getSign(var_name)[field_name]

    if (left_type == "register"):
        res += ["movl " + str(offset+field_offset) + "(%ebp), " + get_register(left_param)]
    elif (left_type == "variable"):
        (var_offset, _), typ = activation_record.getVarTuple(left_param)
        reg = get_register("_tmp")
        res += ["movl " + str(offset+field_offset) + "(%ebp), " + reg]
        res += ["movl " + reg + ", " + str(var_offset) + "(%ebp)"]
        free_register("_tmp")
    else:
        print("Error: Unsupported type", left_type, "of", left_param)
        sys.exit(0)
    return res
