import common
from common import get_register, free_register, getTokType, reserve_register, unreserve_register

def asm_gen(line, activation_record, context, activation_records):
    res = []
    toks = line.split()
    #print(toks)
    # float_regs = ["%st0","%st1","%st2","%st3","%st4","%st5","%st6","%st7"]
    '''
    Some niggas like pow are left out
    '''
    op = "null"
    op_ind = 3
    type_casting = 0
    op1 = ""
    op2 = ""
    if(len(toks) == 6):
        type_casting = 1

    print("typeca", type_casting)
    print()
    if(type_casting == 0):
        if (toks[op_ind][0] == "+"):
            op = "add "
            ty = str(toks[op_ind][1:])
        elif (toks[op_ind][0] == "-"):
            op = "subl "
            ty = str(toks[op_ind][1:])
        elif (toks[op_ind][0] == "*"):
            op = "imul "
            ty = str(toks[op_ind][1:])
        elif (toks[op_ind][0] == "/" or toks[op_ind][0] == "%" or toks[op_ind][0] == "<" or toks[op_ind][0] == ">"):
            op = "handled"
            ty = str(toks[op_ind][1:])
        if op == "null":
            ty = str(toks[op_ind][2:])
    else:
        op2 = toks[5]
        op1 = toks[2]
        if "cast-to" in toks[2]:
            op_ind = 4
            op1 = toks[3]
        if (toks[op_ind][0] == "+"):
            op = "add"
            ty = str(toks[op_ind][1:])
        elif (toks[op_ind][0] == "-"):
            op = "subl"
            ty = str(toks[op_ind][1:])
        elif (toks[op_ind][0] == "*"):
            op = "mul"
            ty = str(toks[op_ind][1:])
        elif (toks[op_ind][0] == "/"):
            op = "div"
            ty = str(toks[op_ind][1:])
        elif (toks[op_ind][0] == "<" or toks[op_ind][0] == ">"):
            op = "inequality"
            ty = str(toks[op_ind][1:])
        if op == "null":
            op = "inequality"
            ty = str(toks[op_ind][2:])

    if "int" in toks[op_ind]:
        ty = "int"
    elif "float" in toks[op_ind]:
        ty = "float"
    elif "bool" in toks[op_ind]:
        ty = "bool"
    elif len(ty) == 0:
        ty = "int"
    else:
        print("Error: bin_op unknown", ty, "of length", len(ty))


    print(ty,toks)
    #print(op)
    # print(ty)
    #print(ty2)
    #print(len(toks))
    if (ty == "int" or ty == "bool"):
        r0 = get_register(toks[0])
        r1 = get_register(toks[2])
        r2 = get_register(toks[4])

        #print("R0 " + r0)
        #print("R1 " + r0)
        #print("R2 " + r0)

        if (toks[3][0] == "+" or toks[3][0] == "-" or toks[3][0] == "*"):
            res.append(op + r2 + ", " + r1)
            res.append("movl "+ r1 + ", " + r0)
        elif (toks[3][0] == "/"):
            reserve_register("%edx")
            reserve_register("%eax")
            free_register(toks[0])
            free_register(toks[2])
            free_register(toks[4])
            r0_0 = get_register(toks[0])
            r1_0 = get_register(toks[2])
            r2_0 = get_register(toks[4])
            res.append("movl " + r0 + ", " + r0_0)
            res.append("movl " + r1 + ", " + r1_0)
            res.append("movl " + r2 + ", " + r2_0)
            r0 = r0_0
            r1 = r1_0
            r2 = r2_0
            res.append("push %edx")
            res.append("push %eax")
            res.append("movl $0, %edx")
            res.append("movl " + r1 + ", %eax")
            res.append("cdq")
            res.append("idiv " + r2)
            res.append("movl %eax, " + r0)
            res.append("pop %eax")
            res.append("pop %edx")
            unreserve_register("%edx")
            unreserve_register("%eax")
        elif (toks[3][0] == '%'):
            reserve_register("%edx")
            reserve_register("%eax")
            free_register(toks[0])
            free_register(toks[2])
            free_register(toks[4])
            r0_0 = get_register(toks[0])
            r1_0 = get_register(toks[2])
            r2_0 = get_register(toks[4])
            res.append("movl " + r0 + ", " + r0_0)
            res.append("movl " + r1 + ", " + r1_0)
            res.append("movl " + r2 + ", " + r2_0)
            r0 = r0_0
            r1 = r1_0
            r2 = r2_0
            res.append("push %edx")
            res.append("push %eax")
            res.append("movl $0, %edx")
            res.append("movl " + r1 + ", %eax")
            res.append("cdq")
            res.append("idiv " + r2)
            res.append("movl %edx, " + r0)
            res.append("pop %eax")
            res.append("pop %edx")
            unreserve_register("%edx")
            unreserve_register("%eax")
            pass
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
            # print("HHHH")
            jmp_instr = {"==": "je", "<": "jg", ">": "jl", "<=": "jge", ">=": "jle", "!=": "jne"}
            if (toks[3][0] in jmp_instr):
                jmp_stmt = jmp_instr[toks[3][0]]
            if (toks[3][0:2] in jmp_instr):
                jmp_stmt = jmp_instr[toks[3][0:2]]
            res.append("cmpl " + r1 + ", " + r2)
            res.append(jmp_stmt + " _rel_op_" + str(context["rel_op_num"]) + "_true")
            res.append("movl $0, " + r0)
            res.append("jmp _rel_op_" + str(context["rel_op_num"]) + "_end")
            res.append("_rel_op_" + str(context["rel_op_num"]) + "_true:")
            res.append("movl $1, " + r0)
            res.append("_rel_op_" + str(context["rel_op_num"]) + "_end:")
            context["rel_op_num"] += 1

        print("Getting freed " + toks[2],toks[4])
        free_register(toks[2])
        free_register(toks[4])


        return res, context

    elif (ty == 'float' and type_casting == 0):
        if (op == "add "):
            res += ["fadd"]
        elif(op == "subl "):
            res += ["fchs"]
            res += ["fadd"]
        elif(op == "imul "):
            res += ["fmul"]
        elif(toks[3][0] == "/"):
            res += ["fdiv " + "%st(1), " + "%st(0)"]
            res += ["fstp " + "%st(0)"]
        elif(toks[3][0:2] == "==" or toks[3][0:2] == "!=" or toks[3][0] == "<" or toks[3][0] == ">" or toks[3][0:2] == "<=" or toks[3][0:2] == ">="):
            jmp_instr = {"==": "je", "<": "jb", ">": "ja", "<=": "jbe", ">=": "jae", "!=": "jne"}
            if (toks[3][0] in jmp_instr):
                jmp_stmt = jmp_instr[toks[3][0]]
            if (toks[3][0:2] in jmp_instr):
                jmp_stmt = jmp_instr[toks[3][0:2]]
            res += ["fxch " + "%st(1)" ]
            res += ["fcomip"]
            res += ["fstp   %st(0)"]
            res.append(jmp_stmt + " _rel_op_" + str(context["rel_op_num"]) + "_true")
            res.append("fldz")
            res.append("jmp _rel_op_" + str(context["rel_op_num"]) + "_end")
            res.append("_rel_op_" + str(context["rel_op_num"]) + "_true:")
            res.append("fld1")
            res.append("_rel_op_" + str(context["rel_op_num"]) + "_end:")
            context["rel_op_num"] += 1


        context["float_stack"].pop()
        context["float_stack"].pop()
        context["float_stack"].append(toks[0])

        return res, context

    elif (ty == 'float' and type_casting == 1):
        op_tobe_cast = -1
        res += ["subl $4, %esp"]
        if op_ind == 3:
            r0 = get_register(toks[5])
            res += ["movl " + r0 + ", (%esp)"]
            op_tobe_cast = 2
        else :
            r0 = get_register(toks[3])
            res += ["movl " + r0 + ", (%esp)"]
            op_tobe_cast = 1
            #print(op)
        if (op == "add"):
            res += ["fiadd (%esp)"]
        elif(op == "subl"):
            if op_tobe_cast == 1:
                res += ["fchs"]
                res += ["fiadd (%esp)"]
            else:
                res += ["negl (%esp)"]
                res += ["fiadd (%esp)"]
        elif(op == "mul"):
            res += ["fimul (%esp)"]
        elif(op == "div"):
            if op_tobe_cast == 1:
                res += ["fidivr (%esp)"]
            else:
                res += ["fidiv (%esp)"]
        elif(op == "inequality"):
            jmp_instr = {"==": "je", "<": "jb", ">": "ja", "<=": "jbe", ">=": "jae", "!=": "jne"}
            if (toks[op_ind][0] in jmp_instr):
                jmp_stmt = jmp_instr[toks[op_ind][0]]
            if (toks[op_ind][0:2] in jmp_instr):
                jmp_stmt = jmp_instr[toks[op_ind][0:2]]

            res += ["fld1"]
            res += ["fimul (%esp)"]
            if op_tobe_cast == 2:
                res += ["fxch " + "%st(1)" ]

            res += ["fcomip"]
            res += ["fstp   %st(0)"]
            res.append(jmp_stmt + " _rel_op_" + str(context["rel_op_num"]) + "_true")
            res.append("fldz")
            res.append("jmp _rel_op_" + str(context["rel_op_num"]) + "_end")
            res.append("_rel_op_" + str(context["rel_op_num"]) + "_true:")
            res.append("fld1")
            res.append("_rel_op_" + str(context["rel_op_num"]) + "_end:")
            context["rel_op_num"] += 1


        if op_ind == 3:
            free_register(toks[5])
        else :
            free_register(toks[3])

        context["float_stack"].pop()
        context["float_stack"].append(toks[0])


            #elif(getTokType(toks[2]) == "variable" and getTokType(toks[4]) == "variable")
        #es+= ["FAIL"]
        return res, context
