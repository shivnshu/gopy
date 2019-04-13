import common
import sys
from common import get_register, set_register, free_register, getTokType
from common import reserve_register, unreserve_register

# Two sources of following truth. Another in common
reserved_words = {"true": "1", "false": "0"}

def asm_gen(line, activation_record, context):
    global reserved_words
    res = []
    toks = line.split(" ", 2) # string support

    left_type = getTokType(toks[0])
    right_type = getTokType(toks[2])
    if (left_type == "register"):
        dst_entry = get_register(toks[0])
    elif (left_type == "variable"):
        (offset, size), typ = activation_record.getVarTuple(toks[0])
        if typ == "global":
            dst_entry = str(offset) + "(%esi)"
        elif typ == "const":
            print("Error: const", toks[0], "can not be assigned")
            sys.exit(0)
        else:
            dst_entry = str(offset) + "(%ebp)"
    elif (left_type == "dereference"):
        if (getTokType(toks[0][1:]) != "variable"):
            print("Error: invalid dereference", toks[0])
            sys.exit(0)
        (offset, size), typ = activation_record.getVarTuple(toks[0][1:])
        if typ == "global":
            dst_entry = str(offset) + "(%esi)"
        elif typ == "const":
            print("Error: const", toks[0], "can not be assigned")
            sys.exit(0)
        else:
            dst_entry = str(offset) + "(%ebp)"
        reg = get_register("_tmp2")
        res += ["movl " + dst_entry + ", " + reg]
        dst_entry = "(" + reg + ")"
    else:
        print("Error: unknown type of", toks[0])
        sys.exit(0)

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
        # print(toks, "with offset", offset)
        if typ == "global":
            src_entry = str(offset) + "(%esi)"
        elif typ == "const":
            src_entry = "$" + toks[2]
        else:
            src_entry = str(offset) + "(%ebp)"
        res.append("movl " + src_entry + ", " + dst_entry)
        if (left_type == "register" and typ == "const"): # Why
            res.append("movl (" + dst_entry + "), " + dst_entry)
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
    elif (right_type == "const"):
        res += ["movl " + "$" + reserved_words[toks[2]] + ", " + dst_entry]
    elif (right_type == "address"):
        if (getTokType(toks[2][1:]) != "variable"):
            print("Error: Address of " + toks[2][1:] + " does not exist")
        else:
            (offset, size), typ = activation_record.getVarTuple(toks[2][1:])
            if (left_type != "variable"):
                res.append("lea " + str(offset) + "(%ebp) ," + dst_entry)
            else:
                reg = get_register("_tmp")
                res.append("lea " + str(offset) + "(%ebp) ," + reg)
                res.append("movl " + reg + ", " + dst_entry)
                free_register("_tmp")

    if (left_type == "dereference"):
        free_register("_tmp2")
    # print(toks, left_type, right_type, res)
    return res, context
