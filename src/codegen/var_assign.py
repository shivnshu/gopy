from common import getTokType, get_register, free_register
import assignments

def asm_gen(line, activation_record, context, data_section, activation_records):
    res = []
    toks = line.split(" ", 2) # string support

    left_type = getTokType(toks[0])
    right_type = getTokType(toks[2])

    if left_type != "variable" or right_type != "variable":
        return assignments.asm_gen(line, activation_record, context, data_section, activation_records)

    # Left Variable
    (offset, jmp), typ = activation_record.getVarTuple(toks[0], activation_records)
    reg_1 = get_register("_left_var")
    res += ["movl %ebp, " + reg_1]
    while (jmp > 0):
        res += ["movl ("+reg_1+"), " + reg_1]
        jmp -= 1

    dst_entry = str(offset) + "(" + reg_1 + ")"
    print("\ndst_entry", dst_entry)
    print(reg_1)

    # Right Variable
    (offset, jmp), typ = activation_record.getVarTuple(toks[2], activation_records)
    reg_2 = get_register("_right_var")
    res += ["movl %ebp, " + reg_2]
    while (jmp > 0):
        res += ["movl (" + reg_2 + "), " + reg_2]
        jmp -= 1
    if typ == "const":
        src_entry = "$" + toks[2]
    else:
        src_entry = str(offset) + "(" + reg_2 + ")"

    print("src_entry", src_entry, "\n")

    reg = get_register("_tmp")
    res.append("movl " + src_entry + ", " + reg)
    res.append("movl " + reg + ", " + dst_entry)
    free_register("_tmp")

    free_register("_right_var")

    return res, context
