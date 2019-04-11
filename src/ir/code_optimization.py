import re

unary_ops = ["+", "-", "!", "^", "*", "&", "<-"]
regex = re.compile(r"_t[0-9]+")

# Specifically handle unary op cases
def unary_optimization(code_list):
    my_dict = {}
    del_list = []
    for i in range(len(code_list)):
        code = code_list[i]
        toks = code.split()
        if (len(toks) != 3 or not ":=" in code):
            continue
        if (toks[2][0] in unary_ops and toks[2][1] == "_"):
            tmp = toks[2][1:]
            code = re.sub(tmp, my_dict[tmp][0], code)
            code_list[i] = code
            del_list += [my_dict[tmp][1]]
            continue
        if (toks[0][0] == "_"):
            my_dict[toks[0]] = (toks[2], i)
    res = []
    for i in range(len(code_list)):
        if not i in del_list:
            res += [code_list[i]]
    return res

def code_optimization(code_list):
    res = []
    first = ""
    last = ""
    for code in code_list:
        toks = code.split()
        if (len(toks) != 3 or not ":=" in code):
            if (len(first) > 0):
                res += [first + " := " + last]
            first = ""
            last = ""
            res += [code]
            continue
        if (len(first) > 0 and first[0] != "_"):
            res += [first + " := " + last]
            first = ""
            last = ""
        if (len(first) == 0):
            first = toks[0]
            last = toks[2]
            continue
        if (first == toks[2]):
            first = toks[0]
            continue
        res += [first + " := " + last]
        first = toks[0]
        last = toks[2]
    res += [first + " := " + last]
    res = unary_optimization(res)
    return res


# code = ['_t0 := 10', '_t1 := _t0', 'a := _t1', '_t2 := a', '_t3 := _t2', '_t4 := _t3', '_t5 := &_t4', 'b := _t5']
# res = code_optimization(code)
# print(res)
