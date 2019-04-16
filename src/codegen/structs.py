import sys
from common import get_register, free_register, getTokType, reserve_register, unreserve_register

size_of = {'int': '4', 'float': '4', 'char': '1', "*int": '4', "*float": '4', "*char": '4', "string": '4'}

def asm_gen(line, activation_record, activation_records):
    res = []
    toks = line.split()
    if ("." in toks[0]):
        var_field = toks[0].split(".")
        var_name = var_field[0]
        field_name = var_field[1]
        assert(getTokType(var_name) == "variable")
        (offset, jmp), typ = activation_record.getVarTuple(var_name, activation_records)
        reg_ = get_register("_pqr")
        res += ["movl %ebp, " + reg_]
        while (jmp > 0):
            res += ["movl ("+reg_+"), " + reg_]
            jmp -= 1
        if (typ == "global" or typ == "const"):
            print("Error: unsupported type", type, "of", var_name)
            sys.exit(0)
        (field_offset, size, typ) = activation_record.getSign(var_name)[field_name]
        right_param = toks[-1]
        right_type = getTokType(right_param)
        if (right_type == "register"):
            reg = get_register("_tmp")
            res += ["movl " + str(offset) + "("+reg_+")" + ", " + reg]
            res += ["add $" + str(field_offset) + ", " + reg]
            res += ["movl " + get_register(right_param) + ", (" + reg + ")"]
            free_register("_tmp")
        elif (right_type == "positive-integer" or right_type == "const"):
            reg = get_register("_tmp")
            res += ["movl " + str(offset) + "("+reg_+")" + ", " + reg]
            res += ["add $" + str(field_offset) + ", " + reg]
            res += ["movl $" + str(right_param) + ", (" + reg + ")"]
            free_register("_tmp")
        elif (right_type == "negative-integer"):
            reg = get_register("_tmp")
            res += ["movl " + str(offset) + "("+reg_+")" + ", " + reg]
            res += ["add $" + str(field_offset) + ", " + reg]
            res += ["movl $" + str(right_param[1:]) + ", (" + reg + ")"]
            res += ["negl (" + reg + ")"]
            free_register("_tmp")
        elif (right_type == "string"):
            string_lit = right_param[1:-1].encode().decode('unicode_escape') # Allow newline etc.
            reserve_register("%eax")
            reg = get_register("_tmp")
            res += ["movl " + str(offset) + "("+reg_+")" + ", " + reg]
            res += ["add $" + str(field_offset) + ", " + reg]
            res += ["push %eax"]
            res += ["push $" + str(len(right_param) + 1)]
            res += ["call malloc"]
            index = 0
            for ch_lit in string_lit:
                res += ["movb $" + hex(ord(ch_lit)) + ", " + str(index) + "(%eax)"]
                index += 1
            res += ["movl %eax, " + "0(" + reg + ")"]
            res += ["pop %eax"]
            free_register("_tmp")
            unreserve_register("%eax")
        else:
            print("Error: unknown type", right_type, "of", toks[-1])
            sys.exit(0)
        free_register("_pqr")
        return res

    # Struct is on right side
    var_field = toks[2].split(".")
    var_name = var_field[0]
    field_name = var_field[1]
    left_param = toks[0]
    left_type = getTokType(left_param)
    assert(getTokType(var_name) == "variable")
    (offset, jmp), typ = activation_record.getVarTuple(var_name, activation_records)
    reg_ = get_register("_pqr")
    res += ["movl %ebp, " + reg_]
    while (jmp > 0):
        res += ["movl ("+reg_+"), " + reg_]
        jmp -= 1
    if (typ == "global" or typ == "const"):
        print("Error: unsupported type", type, "of", var_name)
        sys.exit(0)
    (field_offset, size, typ) = activation_record.getSign(var_name)[field_name]

    if (left_type == "register"):
            reg = get_register("_tmp")
            res += ["movl " + str(offset) + "("+reg_+")" + ", " + reg]
            res += ["add $" + str(field_offset) + ", " + reg]
            res += ["movl (" + reg + "), " + get_register(left_param)]
            free_register("_tmp")
    elif (left_type == "variable"):
        (var_offset, _), typ = activation_record.getVarTuple(left_param, activation_records)
        reg = get_register("_tmp")
        res += ["movl " + str(offset) + "("+reg_+")" + ", " + reg]
        res += ["add $" + str(field_offset) + ", " + reg]
        res += ["movl (" + reg + "), " + reg]
        res += ["movl " + reg + ", " + str(var_offset) + "("+reg_+")"]
        free_register("_tmp")
    else:
        print("Error: Unsupported type", left_type, "of", left_param)
        sys.exit(0)
    free_register("_pqr")
    return res
