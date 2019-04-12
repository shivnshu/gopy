import common
from common import get_register, free_register, getTokType

def asm_gen(line, activation_record, context):
    res = []
    toks = line.split()

    '''
    Some niggas like pow are left out
    '''

    if (toks[3][0] == "+"):
        op = "add "
    elif (toks[3][0] == "-"):
        op = "subl"
    elif (toks[3][0] == "*"):
        op = "imul"

    r0 = get_register(toks[0])
    r1 = get_register(toks[2])
    r2 = get_register(toks[4])

    if (toks[3][0] == "+" or toks[3][0] == "-" or toks[3][0] == "*"):
        res.append(op + r2 + ", " + r1)
        res.append("movl "+ r1 + ", " + r0)
        free_register(toks[2])
        free_register(toks[4])
    elif (toks[3][0] == "/"):
        res.append("push %edx")
        res.append("push %eax")
        res.append("movl " + r1 + ", %edx")
        res.append("movl " + r2 + ", %eax")
        res.append("movl $0, %ebx")
        res.append("movl %edx, %ebx")
        res.append("cltd")
        res.append("idiv %ebx")
        res.append("movl %eax, " + r0)
        res.append("push %eax")
        res.append("push %edx")
    elif (toks[3][0:2] == "||"):
        res.append("cmpl $1, " + r1)
        res.append("je _rel_op_" + str(context["rel_op_num"]) + "_true")
        res.append("cmpl $1, " + r2)
        res.append("je _rel_op_" + str(context["rel_op_num"]) + "_true")
        res.append("movl $0, " + r0)
        res.append("jmp _rel_op_" + str(context["rel_op_num"]) + "_end")
        res.append("_rel_op_" + str(context["rel_op_num"]) + "_true:")
        res.append("movl $1, " + r0)
        res.append("_rel_op_" + str(context["rel_op_num"]) + "_end:")
        context["rel_op_num"] += 1
    elif (toks[3][0:2] == "&&"):
        res.append("cmpl $0, " + r1)
        res.append("je _rel_op_" + str(context["rel_op_num"]) + "_false")
        res.append("cmpl $0, " + r2)
        res.append("je _rel_op_" + str(context["rel_op_num"]) + "_false")
        res.append("movl $1, " + r0)
        res.append("jmp _rel_op_" + str(context["rel_op_num"]) + "_end")
        res.append("_rel_op_" + str(context["rel_op_num"]) + "_false:")
        res.append("movl $0, " + r0)
        res.append("_rel_op_" + str(context["rel_op_num"]) + "_end:")
        context["rel_op_num"] += 1
    elif (toks[3][0:2] == "==" or toks[3][0:2] == "!=" or toks[3][0] == "<" or toks[3][0] == ">" or toks[3][0:2] == "<=" or toks[3][0:2] == ">="):
        jmp_instr = {"==": "je", "<": "jl", ">": "jg", "<=": "jle", ">=": "jge", "!=": "jne"}
        jmp_stmt = jmp_instr[toks[3][0]]
        res.append("cmpl" + r1 + ", " + r2)
        res.append(jmp_stmt + " _rel_op_" + str(context["rel_op_num"]) + "_true")
        res.append("movl $0, " + r0)
        res.append("jmp _rel_op_" + str(context["rel_op_num"]) + "_end")
        res.append("_rel_op_" + str(context["rel_op_num"]) + "_true:")
        res.append("movl $1, " + r0)
        res.append("_rel_op_" + str(context["rel_op_num"]) + "_end:")
        context["rel_op_num"] += 1


    return res, context