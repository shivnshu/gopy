import common
from common import get_register, set_register, free_register, getTokType
from common import reserve_register, unreserve_register

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
        string_lit = toks[2][1:-1].encode().decode('unicode_escape') # Allow newline etc.
        if (left_type == "register"):
            free_register(toks[0])
            reserve_register("%eax")
            dst_entry = get_register(toks[0])
            unreserve_register("%eax")
        res += ["push $" + str(len(string_lit) + 1)]
        res += ["call malloc"]
        index = 0
        for ch_lit in string_lit:
            res += ["movb $" + hex(ord(ch_lit)) + ", " + str(index) + "(%eax)"]
            index += 1
        res += ["movb $0x0, " + str(index) + "(%eax)"]
        res += ["movl %eax, " + dst_entry]
        pass
    return res, context
