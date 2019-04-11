


def get_register(name):
    return "%rax"

def free_register(name):
    pass

def getTokType(tok):
    if (tok[0] == "_"):
        return "register"
    if (tok.isdigit()):
        return "positive-integer"
    if (tok[1:].isdigit() and tok[0] == "-"):
        return "negative-integer"
    if (tok[0] != "'" and tok[0] != '"'):
        return "variable"
    return string
