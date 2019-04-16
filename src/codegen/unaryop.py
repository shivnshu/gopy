import common
from common import get_register, free_register, getTokType, reserve_register, unreserve_register

def asm_gen(line, activation_record, context, activation_records):
    res = []
    toks = line.split()
    # print(toks)

    '''
    Some niggas like pow are left out
    '''
    r0 = get_register(toks[0])
    idx_name = toks[2][1:]
    (offset, jmp), typ = activation_record.getVarTuple(idx_name, activation_records)
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
    if (toks[2][0] == "!"):
        res.append("cmpl $1, " + dst_entry)
        res.append("je _rel_op_" + str(context["rel_op_num"]) + "_true")
        res.append("movl $1, " + r0)
        res.append("jmp _rel_op_" + str(context["rel_op_num"]) + "_end")
        res.append("_rel_op_" + str(context["rel_op_num"]) + "_true:")
        res.append("movl $0, " + r0)
        res.append("_rel_op_" + str(context["rel_op_num"]) + "_end:")
        context["rel_op_num"] += 1
    elif (toks[2][0] == "+"):
        res.append("movl " + dst_entry + ", " + r0)
    elif (toks[2][0] == "-"):
        res.append("movl " + dst_entry + ", " + r0)
        res.append("negl " + r0)

    free_register("_pqr")
    free_register(toks[0])


    return res, context
