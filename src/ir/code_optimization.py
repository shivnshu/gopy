import re

def get_chains(chains):
    if len(chains)>1:
        chains2 = chains[1:]
        count = 0
        for chain in chains[1:]:
            if chains[0][0][0] == chain[0][0]:
                break
            if chains[0][0][0] == chain[-1][1]:
                chains2.remove(chain)
                chains2 = [chain+chains[0]] + chains2
                count += 1
        if count>0:
            return get_chains(chains2)
        else:
            return [chains[0]] + get_chains(chains2)
    else:
        return chains


def get_code(chains):
    code = []
    for chain in chains:
        code += [chain[0][0] + " := " + chain[-1][1]]
    return code


def code_optimization(code):
    code += ["end"]
    code2 = []
    chains = []
    for line in code:
        line2 = re.findall("[a-zA-Z_][a-zA-Z_0-9]* := [a-zA-Z_]?[a-zA-Z_0-9]*", line)
        if line2 != []:
            line2 = line2[0]
        if (line == line2):
            lhs = re.findall("[a-zA-Z_][a-zA-Z_0-9]*", line)[0]
            rhs = re.findall("[a-zA-Z_0-9]+", line)[1]
            chains += [[(lhs, rhs)]]
        else:
            code3 = get_code(get_chains(chains))
            for line_ in code3:
                if line_ not in code2:
                    code2 += [line_]
            code2 += [line]
    code = code2[:-1]
    return code

# code = ['t0 := 1', 't1 := t0', 'a := t1', 't2 := a', 't3 := t2', 't4 := t3', 'push_param t4', '[] := call fmt.Println', 't5 := a', 't6 := t5', 't7 := t6', 'b := t7', 't8 := 10', 't9 := t8', 'd := t9']
# code = code_optimization(code)
# print(code)
