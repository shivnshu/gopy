def get_register(name):
    return "%eax"

def free_register(name):
    pass

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
