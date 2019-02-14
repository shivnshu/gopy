import ply.yacc as yacc

from tokrules import tokens

counter = 0

def p_start(p):
	'''
	Start : Aa token_plus Bb
	'''
	global counter
	p[0] = {"label": "Start", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_aa(p):
	'''
	Aa : INTEGERLIT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_token_plus(p):
	'''
	token_plus : ADD
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_bb(p):
	'''
	Bb : INTEGERLIT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []


def p_error(p):
	print(p)
	print("Syntax error in input!")

parser = yacc.yacc()

