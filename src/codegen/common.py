


def get_register(name):
    return "%rax"

def free_register(name):
    pass

def getTokType(tok):
    if (tok[0] == "_"):
        return "register"
    if (tok.isdigit()):
        return "integer"
    if (tok[0] != "'" and tok[0] != '"'):
        return "variable"
    return string
