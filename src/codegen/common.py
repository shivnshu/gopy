import sys
import re

# %esi store global starting address, that's why not part of usable registers
usable_registers = ["%eax", "%ebx", "%ecx", "%edx", "%edi"]
#free_registers = usable_registers.copy()

reserved_words = {"true": "1", "false": "0"}

register_mapping = {}

def free_all_regs():
    global free_registers
    free_registers = usable_registers.copy()

def get_register(name):
    global free_registers
    global register_mapping
    if (name in register_mapping):
        return register_mapping[name]
    if (len(free_registers) == 0):
        print("Error: out of registers")
        sys.exit(0)
    # print("Debug: get", name)
    register_mapping[name] = free_registers[0]
    free_registers = free_registers[1:]
    return register_mapping[name]

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
    del register_mapping[name]

def reserve_register(reg):
    global free_registers
    if not reg in free_registers:
        print("Error: " + reg + " could not be reserved")
        sys.exit(0)
    free_registers.remove(reg)

def unreserve_register(reg):
    global free_registers
    if reg in free_registers:
        print("Warning: " + reg + " is already unreserved")
    else:
        free_registers += [reg]

binary_op_list = ["+", "-", "*", "/", "&&", "||", "==", "!=", "<", ">", "<=", ">=", "|", "^"]
# assignments
# function call
# binary ops
# return from function
def getCodeType(code):
    code = re.sub(r'".*"', 'string', code)
    toks = code.split()
    if (len(toks) == 3 and ":=" in code):
        return "assignments"
    if (len(toks) == 2 and ("call" in toks or "push_param" in toks or "ret_param" in toks or "ret" in toks or "ret_alloc" in toks)):
        return "function-call"
    if  (len(toks)==5 and toks[1]==":=" and (toks[3][0] in binary_op_list or toks[3][0:2] in binary_op_list)):
        return "binary-op"
    if (toks[0] == "if"):
        return "ifstmt"
    if (toks[0] == "goto"):
        return "gotostmt"
    if (toks[0] == "_decl"):
        return "arr_decl"
    return None

def getTokType(tok):
    global reserved_words
    if (tok[0] == "_"):
        return "register"
    if (tok.isdigit()):
        return "positive-integer"
    if (tok[1:].isdigit() and tok[0] == "-"):
        return "negative-integer"
    if (tok[0] == "'" or tok[0] == '"'):
        return "string"
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
