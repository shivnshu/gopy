import ply.yacc as yacc

from tokrules import tokens

counter = 0

def p_start(p):
	'''
	Start : PackageClause
	'''
	global counter
	p[0] = {"label": "Start", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1]]

def p_package_clause(p):
	'''
	PackageClause  : keyword_package PackageName
	'''
	global counter
	p[0] = {"label": "PackageClause", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_package_name(p):
	'''
	PackageName    : IDENTIFIER
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_package(p):
	'''
	keyword_package : PACKAGE
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []


def p_error(p):
	print(p)
	print("Syntax error in input!")

go_parser = yacc.yacc()

