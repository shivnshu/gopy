import sys
import re

# %esi store global starting address, that's why not part of usable registers
usable_registers = ["%eax", "%ebx", "%ecx", "%edx", "%edi"]

free_registers = usable_registers.copy()
reserved_registers = []

reserved_words = {"true": "1", "false": "0"}

register_mapping = {}

def free_all_regs():
    global free_registers
    free_registers = usable_registers.copy()

def get_register(name):
    global free_registers
    global register_mapping
    global reserved_registers
    if (name in register_mapping):
        return register_mapping[name]
    if (len(free_registers) == 0):
        print("Debug: mapping", register_mapping)
        print("Error: out of registers")
        sys.exit(0)
    # print("Debug: get", name)
    for reg in free_registers:
        if reg not in reserved_registers:
            register_mapping[name] = reg
            free_registers.remove(reg)
            print("Gor Register " + reg)
            return reg
    print("Error: could not find free unreserved register")
    sys.exit(0)

def set_register(name, value):
    if (name in register_mapping):
        print("Error: duplicate entry")
        sys.exit(0)
    register_mapping[name] = value

def free_register(name):
    global free_registers
    global register_mapping
    if (not name in register_mapping):
        print("Debug:", register_mapping)
        print("Error: " + name + " register can not be freed")
        sys.exit(0)
    # print("Debug: free", name)
    if (register_mapping[name] in usable_registers):
        free_registers += [register_mapping[name]]
    print("Freed Register " + register_mapping[name])
    del register_mapping[name]

def reserve_register(reg):
    global reserved_registers
    if reg in reserved_registers:
        return
    reserved_registers += [reg]

def unreserve_register(reg):
    global reserved_registers
    if not reg in reserved_registers:
        print("Warning: " + reg + " not reserved")
    else:
        reserved_registers.remove(reg)

binary_op_list = ["+", "-", "*", "/", "&&", "||", "==", "!=", "<", ">", "<=", ">=", "|", "^", "%"]
unary_op_list = ["+", "-", "!"]

def isAssOrStruct(l_tok, r_tok):
    toks = r_tok.split(".")
    flag = False
    if len(toks) == 1:
        flag = True
    if not flag:
        try:
            int(toks[1])
            return True
        except:
            pass
    toks = l_tok.split(".")
    if len(toks) == 1 and flag:
        return True
    return False


def getCodeType(code):
    code = re.sub(r'".*"', 'string', code)
    toks = code.split()
    if (len(toks) == 3 and ":=" in code and (toks[2][0] not in unary_op_list or getTokType(toks[2][1:]) != "variable") and isAssOrStruct(toks[0], toks[2])):
        return "assignments"
    print(toks, "OMGIN GETCODETYPE")
    if (len(toks) == 3 and ("." in toks[0] or "." in toks[2])):
        return "structs"
    if (len(toks) == 2 and ("call" in toks or "push_param" in toks or "ret_param" in toks or "ret" in toks or "ret_alloc" in toks)):
        return "function-call"
    if  (len(toks)==5 and toks[1]==":=" and (toks[3][0] in binary_op_list or toks[3][0:2] in binary_op_list)):
        return "binary-op"
    if  (len(toks)==6 and toks[1]==":=" and (toks[4][0] in binary_op_list or toks[4][0:2] in binary_op_list)):
        return "binary-op"
    if  (len(toks)==6 and toks[1]==":=" and (toks[3][0] in binary_op_list or toks[3][0:2] in binary_op_list)):
            return "binary-op"
    if (toks[0] == "if"):
        return "ifstmt"
    if (toks[0] == "goto"):
        return "gotostmt"
    if (toks[0] == "_decl" and toks[1] == "array"):
        return "arr_decl"
    if (len(toks)==3 and toks[1]==":=" and (toks[2][0] in unary_op_list) and getTokType(toks[2][1:]) == "variable"):
        return "unary-op"
    if (toks[0] == "_decl"):
        return "struct_decl"
    return None

def getTokType(tok):
    global reserved_words
    if (tok[0] == "'" or tok[0] == '"'):
        return "string"
    if ("[" in tok):
        return "array"
    if (tok[0] == "_"):
        return "register"
    if (tok.isdigit()):
        return "positive-integer"
    if (tok[1:].isdigit() and tok[0] == "-"):
        return "negative-integer"
    if (tok[0] == "&"):
        return "address"
    if (tok[0] == "*"):
        return "dereference"
    if (tok in reserved_words):
        return "const"
    try:
        float(tok)
        return "float"
    except:
        pass
    return "variable"

def getLitType(lit):
    try:
        int(lit)
        return "int"
    except:
        pass
    try:
        float(lit)
        return "float"
    except:
        pass
    if (lit[0] == '"' or lit[0] == "'"):
        return "string"
    print("Error: unknown const type:", lit)
    sys.exit(0)

