import common
import sys
import re
from common import get_register, set_register, free_register, getTokType
from common import reserve_register, unreserve_register

# Two sources of following truth. Another in common
reserved_words = {"true": "1", "false": "0"}

def cal_array_offset(arr_idx, offset, reg, activation_record, dimentions, activation_records):
    res = []
    num_dims = len(arr_idx) - 1
    reg2 = get_register("_tmp2")
    res += ["movl $1, " + reg2]
    res += ["movl $0, " + reg]
    index = len(dimentions) - 1
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
        elif (getTokType(idx_name) == "variable"):
            (offset, jmp), typ = activation_record.getVarTuple(idx_name, activation_records)
            reg_ = get_register("_pqr1")
            res += ["movl %ebp, " + reg_]
            while (jmp > 0):
                res += ["movl ("+reg_+"), " + reg_]
                jmp -= 1
            if typ in ["global", "const"]:
                print("Error: type", typ, "for", idx_name, "is not yet supported")
                sys.exit(0)
            reg3 = get_register("_tmp3")
            res += ["movl " + str(offset) + "(" + reg_ + "), " + reg3]
            res += ["imul " + reg2 + ", " + reg3]
            res += ["add " + reg3 + ", " + reg]
            free_register("_pqr1")
            free_register("_tmp3")
        else:
            print("Error: unknown type", getTokType(idx_name), "of index", idx_name)
            sys.exit(0)
        res += ["imul $" + dimentions[index] + ", " + reg2]
        index -= 1
    free_register("_tmp2")
    return res

def asm_gen(line, activation_record, context, data_section, activation_records):
    global reserved_words
    res = []
    toks = line.split(" ", 2) # string support

    left_type = getTokType(toks[0])
    right_type = getTokType(toks[2])
    # print(toks, left_type, right_type)
    if (left_type == "register"):
        dst_entry = get_register(toks[0])
    elif (left_type == "variable"):
        (offset, jmp), typ = activation_record.getVarTuple(toks[0], activation_records)
        reg_ = get_register("_pqr")
        res += ["movl %ebp, " + reg_]
        while (jmp > 0):
            res += ["movl ("+reg_+"), " + reg_]
            jmp -= 1
        if typ == "global":
            dst_entry = str(offset) + "(%esi)"
        elif typ == "const":
            print("Error: const", toks[0], "can not be assigned")
            sys.exit(0)
        else:
            dst_entry = str(offset) + "("+reg_+")"
        free_register("_pqr")
    elif (left_type == "dereference"):
        if (getTokType(toks[0][1:]) != "variable"):
            print("Error: invalid dereference", toks[0])
            sys.exit(0)
        (offset, jmp), typ = activation_record.getVarTuple(toks[0][1:], activation_records)
        reg_ = get_register("_pqr")
        res += ["movl %ebp, " + reg_]
        while (jmp > 0):
            res += ["movl ("+reg_+"), " + reg_]
            jmp -= 1
        if typ == "global":
            dst_entry = str(offset) + "(%esi)"
        elif typ == "const":
            print("Error: const", toks[0], "can not be assigned")
            sys.exit(0)
        else:
            dst_entry = str(offset) + "("+reg_+")"
        free_register("_pqr")
        reg = get_register("_tmp2")
        res += ["movl " + dst_entry + ", " + reg]
        dst_entry = "(" + reg + ")"
    elif (left_type == "array"):
        arr_idx = re.split("\[|\]", toks[0])
        arr_idx = list(filter(None, arr_idx))
        dimentions = context["array_decl"][arr_idx[0]]["dimentions"]
        if (len(dimentions) != len(arr_idx)-1):
            print("Error: dimentions mismatch for array", arr_idx[0])
            sys.exit(0)
        (offset, jmp), typ = activation_record.getVarTuple(arr_idx[0], activation_records)
        reg_ = get_register("_pqr")
        res += ["movl %ebp, " + reg_]
        while (jmp > 0):
            res += ["movl ("+reg_+"), " + reg_]
            jmp -= 1
        if (typ == "global" or typ == "const"):
            print("Error: unsupported code", line)
            sys.exit(0)
        reg = get_register("_tmp_left")
        res += cal_array_offset(arr_idx, offset, reg, activation_record, dimentions, activation_records)
        res += ["imul $" + context["array_decl"][arr_idx[0]]["size"] + ", " + reg]
        res += ["add " + str(offset) + "("+reg_+"), " + reg]
        free_register("_pqr")
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
        (offset, jmp), typ = activation_record.getVarTuple(toks[2], activation_records)
        # print(toks, "with offset", offset)
        reg_ = get_register("_pqr")
        res += ["movl %ebp, " + reg_]
        while (jmp > 0):
            res += ["movl ("+reg_+"), " + reg_]
            jmp -= 1
        if typ == "global":
            src_entry = str(offset) + "(%esi)"
        elif typ == "const":
            src_entry = "$" + toks[2]
        else:
            src_entry = str(offset) + "("+reg_+")"
        free_register("_pqr")
        if (left_type != "variable" and left_type != "dereference" and left_type != "array"):
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
            (offset, jmp), typ = activation_record.getVarTuple(toks[2][1:], activation_records)
            reg_ = get_register("_pqr")
            res += ["movl %ebp, " + reg_]
            while (jmp > 0):
                res += ["movl ("+reg_+"), " + reg_]
                jmp -= 1
            if (left_type != "variable"):
                res.append("lea " + str(offset) + "("+reg_+") ," + dst_entry)
            else:
                reg = get_register("_tmp")
                res.append("lea " + str(offset) + "("+reg_+") ," + reg)
                res.append("movl " + reg + ", " + dst_entry)
                free_register("_tmp")
            free_register("_pqr")
    elif (right_type == "float"):
        # res.append("mov $" + toks[2] + " ," + reg)
        # res.append("fld " + "$" + toks[2] + "")
        # res.append("fstp " + dst_entry)
        float_name = "float_" + str(context["counter"])
        context["counter"] += 1
        data_section += [float_name + ": .float " + toks[2]]
    elif (right_type == "array"):
        arr_idx = re.split("\[|\]", toks[2])
        arr_idx = list(filter(None, arr_idx))
        (offset, jmp), typ = activation_record.getVarTuple(arr_idx[0], activation_records)
        reg = get_register("_tmp_right")
        dimentions = context["array_decl"][arr_idx[0]]["dimentions"]
        res += cal_array_offset(arr_idx, offset, reg, activation_record, dimentions, activation_records)

        reg_ = get_register("_pqr")
        res += ["movl %ebp, " + reg_]
        while (jmp > 0):
            res += ["movl ("+reg_+"), " + reg_]
            jmp -= 1
        if (typ != "global" and typ != "const"):
            pass
        res += ["imul $" + context["array_decl"][arr_idx[0]]["size"] + ", " + reg]
        res += ["add " + str(offset) + "("+reg_+"), " + reg]
        free_register("_pqr")
        if "(" in dst_entry:
            reg10 = get_register("_tmp10")
            res += ["movl 0(" + reg + "), " + reg10]
            res += ["movl " + reg10 + ", " + dst_entry]
            free_register("_tmp10")
        else:
            res += ["movl 0(" + reg + "), " + dst_entry]
    elif (right_type == "dereference"):
        if (getTokType(toks[2][1:]) != "variable"):
            print("Error: dereference of non variable", toks[2][1:])
            sys.exit(0)
        reg_ = get_register("_pqr")
        (offset, jmp), typ = activation_record.getVarTuple(toks[2][1:], activation_records)
        res += ["movl %ebp, " + reg_]
        while (jmp > 0):
            res += ["movl ("+reg_+"), " + reg_]
            jmp -= 1
        if (typ == "global" or typ == "const"):
            print("Error: unsupported code", line)
            sys.exit(0)
        reg = get_register("_tmp")
        res += ["movl " + str(offset) + "("+reg_+"), " + reg]
        res += ["movl 0(" + reg + "), " + reg]
        res += ["movl " + reg + ", " + dst_entry]
        free_register("_tmp")
        free_register("_pqr")
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
