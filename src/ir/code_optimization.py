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

# Specifically handle array
def array_optimization(code_list):
    my_dict = {}
    mapping = {}
    del_list = []
    res = []
    for i in range(len(code_list)):
        code = code_list[i]
        toks = code.split()
        if (len(toks) != 3 or not ":=" in code):
            res += [code]
            continue
        mapping[toks[0]] = (toks[2], i)
        if not "[" in toks[2]:
            res += [code]
        else:
            arr_idx = re.split("\[|\]", toks[2])
            arr_idx = list(filter(None, arr_idx))
            this_code = toks[0] + " := " + mapping[arr_idx[0]][0]
            del_list += [mapping[arr_idx[0]][1]]
            for dim in range(1, len(arr_idx)):
                this_code += '[' + mapping[arr_idx[dim]][0] + ']'
                del_list += [mapping[arr_idx[dim]][1]]
            res += [this_code]
            mapping[toks[0]] = (this_code.split()[2], i)
    final_res = []
    for i in range(len(res)):
        if not i in del_list:
            final_res += [res[i]]
    return final_res

def code_optimization(code_list):
    # print()
    # for c in code_list:
    #     print(c)
    # print()
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
    if (first != ""):
        res += [first + " := " + last]
    res = unary_optimization(res)
    res = array_optimization(res)
    return res


# code = ['_t0 := 10', '_t1 := _t0', 'a := _t1', '_t2 := a', '_t3 := _t2', '_t4 := _t3', '_t5 := &_t4', 'b := _t5']
# res = code_optimization(code)
# print(res)
