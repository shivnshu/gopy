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

    code_list = final_res
    res = []
    del_list = []
    my_map = {}
    for i in range(len(code_list)):
        code = code_list[i]
        toks = code.split()
        if len(toks) != 3 and toks[0] != "_decl" and len(toks) > 1 and toks[1] != "array":
            res += [code]
            continue
        if len(toks) == 3 and toks[0][0] == "_" and toks[1] == ":=":
            my_map[toks[0]] = (toks[2], i)
            res += [code]
            continue
        if len(toks) > 1 and toks[0] == "_decl" and toks[1] == "array":
            new_code = "_decl array " + toks[2] + " " + toks[3]
            for j in range(4, len(toks)):
                if toks[j][0] == "_":
                    new_code += " " + my_map[toks[j]][0]
                    del_list += [my_map[toks[j]][1]]
                else:
                    new_code += " " + toks[j]
            res += [new_code]
        else:
            res += [code]

    final_res = []
    for i in range(len(res)):
        if i not in del_list:
            final_res += [res[i]]

    return final_res

def struct_optimization(code_list):
    res = []
    del_list = []
    for i in range(len(code_list)):
        line = code_list[i]
        toks = line.split()
        if (len(toks) != 3 or "." not in toks[0]):
            res += [line]
            continue
        struct_toks = toks[0].split(".")
        struct_reg_name = struct_toks[0]
        if struct_reg_name[0] != "_": # Not register
            res += [line]
            continue
        # Search forward
        found = False
        var_name = ''
        for j in range(i+1, len(code_list)):
            ass_line = code_list[j]
            ass_line_toks = ass_line.split()
            if (len(ass_line_toks) != 3 or ":=" not in ass_line_toks):
                continue
            if struct_reg_name == ass_line_toks[2]:
                found = True
                del_list += [j]
                var_name = ass_line_toks[0]
                break
        if not found:
            print("Error: while optimizing structs. Try removing this optimization")
            sys.exit(0)
        line = re.sub(struct_reg_name, var_name, line)
        res += [line]
    final_res = []
    for i in range(len(res)):
        if i not in del_list:
            final_res += [res[i]]
    return final_res

def func_optimization(code_list):
    res = []
    del_list = []
    mapping = {}
    for i in range(len(code_list)):
        line = code_list[i]
        toks = line.split()
        if (len(toks) != 3 and len(toks) != 2):
            res += [line]
            continue
        if (len(toks) == 3 and toks[1] == ":="):
            if (toks[0][0] != "_"):
                res += [line]
                continue
            mapping[toks[0]] = (toks[2], i)
            res += [line]
        elif (len(toks) == 2 and toks[0] == "push_param"):
            if (toks[1][0] == "_" and toks[1] in mapping):
                res += ["push_param " + mapping[toks[1]][0]]
                del_list += [mapping[toks[1]][1]]
                continue
        else:
            res += [line]
    final_res = []
    for i in range(len(res)):
        if i not in del_list:
            final_res += [res[i]]
        pass
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
    res = struct_optimization(res)
    # res = func_optimization(res)
    return res


# code = ['_t0 := 10', '_t1 := _t0', 'a := _t1', '_t2 := a', '_t3 := _t2', '_t4 := _t3', '_t5 := &_t4', 'b := _t5']
# res = code_optimization(code)
# print(res)
