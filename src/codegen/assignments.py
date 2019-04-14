import common
import sys
import re
from common import get_register, set_register, free_register, getTokType
from common import reserve_register, unreserve_register

# Two sources of following truth. Another in common
reserved_words = {"true": "1", "false": "0"}

def cal_array_offset(arr_idx, offset, reg):
    res = []
    num_dims = len(arr_idx) - 1
    dim_offset = offset + num_dims * 4
    reg2 = get_register("_tmp2")
    res += ["movl $1, " + reg2]
    res += ["movl $0, " + reg]
    for i in range(num_dims):
        idx_name = arr_idx[num_dims - i]
        if (getTokType(idx_name) == "register"):
            res += ["imul " + reg2 + ", " + get_register(idx_name)]
            res += ["add " + get_register(idx_name) + ", "  + reg]
            free_register(idx_name)
        elif (getTokType(idx_name) == "positive-integer"):
            reg3 = get_register("_tmp3")
            res += ["movl $" + idx_name + ", " + reg3]
            res += ["imul " + reg2 + ", " + reg3]
            res += ["add " + reg3 + ", "  + reg]
            free_register("_tmp3")
        else:
            print("Error: unknown type of index", idx_name)
            sys.exit(0)
        res += ["imul " + str(dim_offset) + "(%ebp), " + reg2]
        dim_offset -= 4
    free_register("_tmp2")
    return res

def asm_gen(line, activation_record, context):
    global reserved_words
    res = []
    toks = line.split(" ", 2) # string support

    left_type = getTokType(toks[0])
    right_type = getTokType(toks[2])
    print(toks, left_type, right_type)
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
    elif (left_type == "array"):
        arr_idx = re.split("\[|\]", toks[0])
        arr_idx = list(filter(None, arr_idx))
        # print(arr_idx)
        (offset, size), typ = activation_record.getVarTuple(arr_idx[0])
        if (size != 4 * len(arr_idx)):
            print("Error: dimension mismatch for array", arr_idx[0])
            sys.exit(0)
        idx_offset = offset + 4
        if (typ != "global" and typ != "const"):
            # Dim ranges check
            pass
        reg = get_register("_tmp_left")
        res += cal_array_offset(arr_idx, offset, reg)
        res += ["imul $" + context["array_decl"][arr_idx[0]] + ", " + reg]
        res += ["add " + str(offset) + "(%ebp), " + reg]
        dst_entry = "0(" + reg + ")"
        pass
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
        if (left_type != "variable" and left_type != "dereference"):
            res.append("movl " + src_entry + ", " + dst_entry)
        else:
            reg = get_register("_tmp")
            res.append("movl " + src_entry + ", " + reg)
            res.append("movl " + reg + ", " + dst_entry)
            free_register("_tmp")
        if (left_type == "register" and typ == "const" and context["const_decl"][toks[2]] != "string"): # Why
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
    elif (right_type == "float"):
        res.append("mov $" + toks[2] + " ," + reg)
        res.append("fld " + "$" + toks[2] + "")
        res.append("fstp " + dst_entry)
    elif (right_type == "array"):
        arr_idx = re.split("\[|\]", toks[2])
        arr_idx = list(filter(None, arr_idx))
        (offset, size), typ = activation_record.getVarTuple(arr_idx[0])
        if (typ != "global" and typ != "const"):
            pass
        reg = get_register("_tmp_right")
        res += cal_array_offset(arr_idx, offset, reg)
        res += ["imul $" + context["array_decl"][arr_idx[0]] + ", " + reg]
        res += ["add " + str(offset) + "(%ebp), " + reg]
        res += ["movl 0(" + reg + "), " + dst_entry]
    elif (right_type == "dereference"):
        print("defe")
        if (getTokType(toks[2][1:]) != "variable"):
            print("Error: dereference of non variable", toks[2][1:])
            sys.exit(0)
        (offset, size), typ = activation_record.getVarTuple(toks[2][1:])
        if (typ != "global" and typ != "const"):
            pass
        reg = get_register("_tmp")
        res += ["movl " + str(offset) + "(%ebp), " + reg]
        res += ["movl 0(" + reg + "), " + reg]
        res += ["movl " + reg + ", " + dst_entry]
        free_register("_tmp")
    else:
        print("Error: Unknown right hand type", toks[2])
        sys.exit(0)

    if (left_type == "dereference"):
        free_register("_tmp2")
    if (left_type == "array"):
        free_register("_tmp_left")
    if (right_type == "array"):
        free_register("_tmp_right")
    # print(toks, left_type, right_type, res)
    return res, context
