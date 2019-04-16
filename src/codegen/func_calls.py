import sys
from common import get_register, free_register, getTokType, reserve_register, unreserve_register
import assignments

def asm_gen(line, activation_record, func_name, context, data_section, activation_records):
    res = []
    toks = line.split()
    if (len(toks) != 2):
        return res, context
    if (toks[0] == "call"):
        if (toks[1][0:4] != "fmt."):
            context["last_func_call_ret"] = activation_records[toks[1]].getRetValues()
            context["last_func_call_ret_offset"] = 0
        else:
            toks[1] = toks[1][4:]
        res += [toks[0] + " " + toks[1]]
    elif (toks[0] == "push_param"):
        param_type = getTokType(toks[1])
        if (param_type == "register"):
            if toks[1] in context["float_stack"]:
                res += ["subl $4, %esp"]
                res += ["fstp (%esp)"]
            else:
                res += ["push " + get_register(toks[1])]
                free_register(toks[1])
        elif (param_type == "variable"):
            (offset, size), typ = activation_record.getVarTuple(toks[1], activation_records)
            if typ == "global":
                reg = get_register("_qwerty")
                res += ["movl " + str(offset) + "(%esi), " + reg]
                res += ["push " + reg]
                free_register("_qwerty")
                return res, context
            elif typ == "const":
                if context["const_decl"][toks[1]] == "string":
                    res += ["push $" + toks[1]]
                else:
                    reg_1 = get_register("_p")
                    res += ["movl $" + toks[1] + ", " + reg_1]
                    res += ["push (" + reg_1 + ")"]
            else:
                res += ["push " + str(offset) + "(%ebp)"]
        elif (param_type == "positive-integer"):
            res += ["push " + "$" + toks[1]]
        elif (param_type == "address"):
            assert(getTokType(toks[1][1:]) == "variable")
            (offset, size), typ = activation_record.getVarTuple(toks[1][1:], activation_records)
            reg = get_register("_push_param")
            res += ["movl %ebp, " + reg]
            res += ["add $" + str(offset) + ", " + reg]
            res += ["push " + reg]
            free_register("_push_param")
        elif (param_type == "string"):
            reserve_register("%eax")
            reg = get_register("_push_param")
            string_lit = toks[1].encode().decode('unicode_escape') # Allow newline etc.
            res += ["push %eax"]
            res += ["subl $4, %esp"]
            res += ["push $" + str(len(string_lit) + 1)]
            res += ["call malloc"]
            index = 0
            for ch_lit in string_lit:
                res += ["movb $" + hex(ord(ch_lit)) + ", " + str(index) + "(%eax)"]
                index += 1
            res += ["movb $0x0, " + str(index) + "(%eax)"]
            res += ["movl %eax, " + reg]
            res += ["pop %eax"]
            res += ["push " + reg]
            free_register("_push_param")
            unreserve_register("%eax")
        else:
            print("Error: push_param", toks[1], "type", param_type, "not supported")
            sys.exit(0)
    elif (toks[0] == "ret_param"):
        (offset, _) = context["last_func_call_ret"][0]
        ret_offset = context["last_func_call_ret_offset"]
        context["last_func_call_ret"] = context["last_func_call_ret"][1:]
        param_type = getTokType(toks[1])
        if (param_type == "register"):
            res += ["movl " + str(offset - 8) + "(%esp), " + get_register(toks[1])]
        elif (param_type == "variable"):
            (offset, _), typ = activation_record.getVarTuple(toks[1], activation_records)
            if typ == "global" or typ == "const":
                print("Error: unsupported code", line)
                sys.exit(0)
            else:
                res += ["movl ", + str(ret_offset) + "(%ebp), " + str(offset) + "(%ebp)"]

    elif (toks[0] == "ret"):
        if (len(context["func_ret"]) == 0):
            context["func_ret"] = activation_records[func_name].getRetValues()
        (ret_offset, _) = context["func_ret"][0]
        context["func_ret"] = context["func_ret"][1:]
        param_type = getTokType(toks[1])
        if (param_type == "register"):
            res += ["movl " + get_register(toks[1]) + ", " + str(ret_offset) + "(%ebp)"]
            free_register(toks[1])
        else:
            print("Error:", toks[0], "type not known")
            sys.exit(0)
    elif (toks[0] == "ret_alloc"):
        res += ["subl $" + toks[1] + ", %esp"]
    return res, context
