from common import getTokType, get_register, free_register

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
    res = []
    toks = line.split(" ", 2) # string support

    left_type = getTokType(toks[0])
    right_type = getTokType(toks[2])

    assert(left_type == "array" or right_type == "array")

    # Left array
    arr_idx = re.split("\[|\]", toks[0])
    arr_idx = list(filter(None, arr_idx))
    dimentions = context["array_decl"][arr_idx[0]]["dimentions"]
    if (len(dimentions) != len(arr_idx)-1):
        print("Error: dimentions mismatch for array", arr_idx[0])
        sys.exit(0)
    (offset, jmp), typ = activation_record.getVarTuple(arr_idx[0], activation_records)
    reg_1 = get_register("_arr_left")
    res += ["movl %ebp, " + reg_1]
    while (jmp > 0):
        res += ["movl (" + reg_1 + "), " + reg_1]
        jmp -= 1
    if (typ == "const"):
        print("Error: unsupported code", line)
        sys.exit(0)

    reg = get_register("_tmp_left")
    res += cal_array_offset(arr_idx, offset, reg, activation_record, dimentions, activation_records)
    res += ["imul $" + context["array_decl"][arr_idx[0]]["size"] + ", " + reg]
    res += ["add " + str(offset) + "("+reg_+"), " + reg]
    dst_entry = "0(" + reg + ")"


    return res, context
