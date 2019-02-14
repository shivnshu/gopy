import ply.yacc as yacc

from tokrules import tokens

counter = 0

def p_empty(p):
	'empty :'
	pass

def p_keyword_package(p):
	'''
	keyword_package : PACKAGE
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_identifier(p):
	'''
	keyword_identifier : IDENTIFIER
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_import(p):
	'''
	keyword_import : IMPORT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_lparen(p):
	'''
	keyword_lparen : LPAREN
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_rparen(p):
	'''
	keyword_rparen : RPAREN
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_dot(p):
	'''
	keyword_dot : DOT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_source_file(p):
	'''
	SourceFile    : PackageClause ImportDeclList
	'''
	global counter
	p[0] = {"label": "SourceFile", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_package_clause(p):
	'''
	PackageClause  : keyword_package keyword_identifier
	'''
	global counter
	p[0] = {"label": "PackageClause", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_import_decl_list(p):
	'''
	ImportDeclList : ImportDecl ImportDeclList
	               | empty
	'''
	global counter
	p[0] = {"label": "ImportDeclList", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_top_level_decl_list(p):
	'''
	TopLevelDeclList : STRINGLIT TopLevelDeclList
	                 | empty
	'''
	global counter
	p[0] = {"label": "TopLevelDeclList", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_import_decl(p):
	'''
	ImportDecl    : keyword_import ImportSpecTopList
	'''
	global counter
	p[0] = {"label": "ImportDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_import_spec_top_list(p):
	'''
	ImportSpecTopList : ImportSpec
	                  | keyword_lparen ImportSpecList keyword_rparen 
	'''
	global counter
	p[0] = {"label": "ImportSpecTopList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1], p[2], p[3]]

def p_import_spec_list(p):
	'''
	ImportSpecList : ImportSpec ImportSpecList
	               | empty
	'''
	global counter
	p[0] = {"label": "ImportSpecList", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_import_spec(p):
	'''
	ImportSpec       :  ImportSpecInit ImportPath
	'''
	global counter
	p[0] = {"label": "ImportSpec", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_import_spec_init(p):
	'''
	ImportSpecInit : keyword_dot
	               | keyword_identifier
	               | empty
	'''
	global counter
	p[0] = {"label": "ImportSpecInit", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_import_path(p):
	'''
	ImportPath     : STRINGLIT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []


def p_error(p):
	print(p)
	print("Syntax error in input!")

go_parser = yacc.yacc(start="SourceFile")

