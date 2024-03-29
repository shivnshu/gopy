import sys
from common import get_register, free_register, getTokType, reserve_register, unreserve_register

size_of = {'int': '4', 'float': '4', 'char': '1', "*int": '4', "*float": '4', "*char": '4', "string": '4'}

def asm_gen(line, activation_record, context, activation_records, data_section):
    res = []
    toks = line.split()
    if ("." in toks[0]):
        var_field = toks[0].split(".")
        var_name = var_field[0]
        field_name = var_field[1]
        assert(getTokType(var_name) == "variable")
        (offset, size), typ = activation_record.getVarTuple(var_name, activation_records)
        if (typ == "global" or typ == "const"):
            print("Error: unsupported type", type, "of", var_name)
            sys.exit(0)
        (field_offset, size, typ) = activation_record.getSign(var_name)[field_name]
        right_param = toks[-1]
        right_type = getTokType(right_param)
        if (right_type == "register"):
            reg = get_register("_tmp")
            res += ["movl " + str(offset) + "(%ebp)" + ", " + reg]
            res += ["add $" + str(field_offset) + ", " + reg]
            res += ["movl " + get_register(right_param) + ", (" + reg + ")"]
            free_register("_tmp")
        elif (right_type == "positive-integer" or right_type == "const"):
            reg = get_register("_tmp")
            res += ["movl " + str(offset) + "(%ebp)" + ", " + reg]
            res += ["add $" + str(field_offset) + ", " + reg]
            res += ["movl $" + str(right_param) + ", (" + reg + ")"]
            free_register("_tmp")
        elif (right_type == "negative-integer"):
            reg = get_register("_tmp")
            res += ["movl " + str(offset) + "(%ebp)" + ", " + reg]
            res += ["add $" + str(field_offset) + ", " + reg]
            res += ["movl $" + str(right_param[1:]) + ", (" + reg + ")"]
            res += ["negl (" + reg + ")"]
            free_register("_tmp")
        elif (right_type == "string"):
            string_lit = right_param[1:-1].encode().decode('unicode_escape') # Allow newline etc.
            reserve_register("%eax")
            reg = get_register("_tmp")
            res += ["movl " + str(offset) + "(%ebp)" + ", " + reg]
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
        elif right_type == "variable":
            (var_offset, _), typ = activation_record.getVarTuple(right_param, activation_records)
            reg = get_register("_tmp")
            res += ["movl " + str(offset) + "(%ebp)" + ", " + reg]
            res += ["add $" + str(field_offset) + ", " + reg]
            if typ == "const":
                res += ["movl $" + right_param + ", (" + reg + ")"]
            elif typ == "global":
                reg2 = get_register("_tmp2")
                res += ["movl " + str(var_offset) + "(%esi), " + reg2]
                res += ["movl " + reg2 + ", (" + reg + ")"]
                free_register("_tmp2")
            else:
                reg2 = get_register("_tmp2")
                res += ["movl " + str(var_offset) + "(%ebp), " + reg2]
                res += ["movl " + reg2 + ", (" + reg + ")"]
                free_register("_tmp2")
            free_register("_tmp")
        elif right_type == "float":
            float_name = "float_" + str(context["counter"])
            context["counter"] += 1
            data_section += [float_name + ": .float " + toks[2]]
            res += ["fld" + " " + float_name]
            reg = get_register("_tmp")
            res += ["movl " + str(offset) + "(%ebp)" + ", " + reg]
            res += ["add $" + str(field_offset) + ", " + reg]
            res += ["fstp (" + reg + ")"]
            free_register("_tmp")
            context["float_vals"].append(toks[0])
        else:
            print("Error: unknown type", right_type, "of", toks[-1])
            sys.exit(0)
        return res, context

    # Struct is on right side
    var_field = toks[2].split(".")
    var_name = var_field[0]
    field_name = var_field[1]
    left_param = toks[0]
    left_type = getTokType(left_param)
    assert(getTokType(var_name) == "variable")
    (offset, size), typ = activation_record.getVarTuple(var_name, activation_records)
    if (typ == "global" or typ == "const"):
        print("Error: unsupported type", type, "of", var_name)
        sys.exit(0)
    (field_offset, size, typ) = activation_record.getSign(var_name)[field_name]

    if (left_type == "register"):
            reg = get_register("_tmp")
            res += ["movl " + str(offset) + "(%ebp)" + ", " + reg]
            res += ["add $" + str(field_offset) + ", " + reg]
            res += ["movl (" + reg + "), " + get_register(left_param)]
            free_register("_tmp")
    elif (left_type == "variable"):
        (var_offset, _), typ = activation_record.getVarTuple(left_param, activation_records)
        reg = get_register("_tmp")
        res += ["movl " + str(offset) + "(%ebp)" + ", " + reg]
        res += ["add $" + str(field_offset) + ", " + reg]
        res += ["movl (" + reg + "), " + reg]
        res += ["movl " + reg + ", " + str(var_offset) + "(%ebp)"]
        free_register("_tmp")
    else:
        print("Error: Unsupported type", left_type, "of", left_param)
        sys.exit(0)
    return res, context
