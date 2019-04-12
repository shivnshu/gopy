import sys

usable_registers = ["%eax", "%ebx", "%ecx", "%edx", "%esi", "%edi"]
free_registers = usable_registers.copy()

register_mapping = {}

def get_register(name):
    global free_registers
    global register_mapping
    if (name in register_mapping):
        return register_mapping[name]
    if (len(free_registers) == 0):
        print("Error: out of registers")
        sys.exit(0)
    register_mapping[name] = free_registers[0]
    free_registers = free_registers[1:]
    return register_mapping[name]

def free_register(name):
    global free_registers
    global register_mapping
    if (not name in register_mapping):
        print("Error: register can not be freed")
        sys.exit(0)
    free_registers += [register_mapping[name]]
    del register_mapping[name]

# assignments
# function call
# binary ops
# return from function
def getCodeType(code):
    toks = code.split()
    if (len(toks) == 3 and ":=" in code):
        return "assignments"
    if (len(toks) == 2 and ("call" in toks or "push_param" in toks or "ret_param" in toks or "ret" in toks)):
        return "function-call"
    return None

def getTokType(tok):
    if (tok[0] == "_"):
        return "register"
    if (tok.isdigit()):
        return "positive-integer"
    if (tok[1:].isdigit() and tok[0] == "-"):
        return "negative-integer"
    if (tok[0] != "'" and tok[0] != '"'):
        return "variable"
    return "string"
