import common
from common import get_register, set_register, free_register, getTokType

def asm_gen(line, activation_record, context, data_section):
    res = []
    toks = line.split(" ", 2) # string support
    # print(toks)

    left_type = getTokType(toks[0])
    right_type = getTokType(toks[2])
    if (left_type == "register"):
        dst_entry = get_register(toks[0])
    elif (left_type == "variable"):
        (offset, size), typ = activation_record.getVarTuple(toks[0])
        if typ == "global":
            pass
        else:
            dst_entry = str(offset) + "(%ebp)"

    if (right_type == "register"):
        src_entry = get_register(toks[2])
        free_register(toks[2])
        res.append("movl " + src_entry + ", " + dst_entry)
    elif (right_type == "positive-integer"):
        src_entry = "$" + toks[2]
        res.append("movl " + src_entry + ", " + dst_entry)
    elif (right_type == "negative-integer"):
        src_entry = "$" + toks[2][1:]
        res.append("movl " + src_entry + ", " + dst_entry)
        res.append("negl " + dst_entry)
    elif (right_type == "variable"):
        (offset, size), typ = activation_record.getVarTuple(toks[2])
        if typ == "global":
            pass
        else:
            src_entry = str(offset) + "(%ebp)"
            res.append("movl " + src_entry + ", " + dst_entry)
    elif (right_type == "string"):
        string_name = "string_" + str(context["num"])
        data_section += [string_name + ': .string ' + toks[2]]
        context["num"] += 1
        free_register(toks[0])
        set_register(toks[0], "$" + string_name)
    return res, context
