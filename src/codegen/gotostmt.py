from common import get_register, free_register, getTokType

def asm_gen(line, activation_records):
	res = []
	toks = line.split()
	res.append("jmp " + toks[1])
	return res
