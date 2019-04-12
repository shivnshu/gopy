import sys
from common import get_register, free_register, getTokType

def asm_gen(line, activation_records, func_name, context):
    res = []
    toks = line.split()
    activation_record = activation_records[func_name]
    if (len(toks) != 2):
        return res, context
    if (toks[0] == "call"):
        context["last_func_call_ret"] = activation_records[toks[1]].getRetValues()
        context["last_func_call_ret_offset"] = 0
        res += [line]
    if (toks[0] == "push_param"):
        param_type = getTokType(toks[1])
        if (param_type == "register"):
            res += ["push " + get_register(toks[1])]
            free_register(toks[1])
        elif (param_type == "variable"):
            (offset, size), typ = activation_record.getVarTuple(toks[1])
            if typ == "global":
                pass
            else:
                res += ["push " + str(offset) + "(%ebp)"]
        elif (param_type == "positive-integer"):
            res += ["push ", "$" + toks[1]]
        else:
            print("Error")
            sys.exit(0)
    if (toks[0] == "ret_param"):
        (_, ret_size) = context["last_func_call_ret"][0]
        ret_offset = context["last_func_call_ret_offset"]
        context["last_func_call_ret_offset"] += ret_size
        context["last_func_call_ret"] = context["last_func_call_ret"][1:]
        param_type = getTokType(toks[1])
        if (param_type == "register"):
            res += ["movl " + str(ret_offset) + "(%esp), " + get_register(toks[1])]
        elif (param_type == "variable"):
            (offset, _), typ = activation_record.getVarTuple(toks[1])
            if typ == "global":
                pass
            else:
                res += ["movl ", + str(ret_offset) + "(%ebp), " + str(offset) + "(%ebp)"]

    if (toks[0] == "ret"):
        if (len(context["func_ret"]) == 0):
            context["func_ret"] = activation_record.getRetValues()
        (ret_offset, _) = context["func_ret"][0]
        context["func_ret"] = context["func_ret"][1:]
        param_type = getTokType(toks[1])
        if (param_type == "register"):
            res += ["movl " + get_register(toks[1]) + ", " + str(ret_offset) + "(%ebp)"]
        else:
            print("Error")
            sys.exit(0)
    return res, context
