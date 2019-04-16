import ply.yacc as yacc
import sys
from tokrules import tokens

from SymbolTable import SymbolTable
from SymbolTable import SymbolTableLitEntry as LitEntry
from SymbolTable import SymbolTableVariableEntry as VarEntry
from SymbolTable import SymbolTableInterfaceEntry as InterfaceEntry
from SymbolTable import SymbolTableStructEntry as StructEntry
from SymbolTable import SymbolTableFunctionEntry as FuncEntry
from SymbolTable import SymbolTableImportEntry as ImportEntry

from SymbolTable import ActivationRecord
from utils import symTableToCSV
from code_optimization import code_optimization

symTableDict = {'rootSymTable': SymbolTable(None, 'rootSymTable')}
symTableSt = ['rootSymTable']
actRecordDict = {'root': ActivationRecord('root', None)}
actRecordSt = ['root']
counter = 0
label_counter = 0

beglabel = ''
endlabel = ''
def newVar():
	global counter
	res = '_t' + str(counter)
	counter += 1
	return res

def newLabel():
	global label_counter
	res = '_label' + str(label_counter)
	label_counter += 1
	return res

def verifyCalType(name, lineno):
	toks = name.split('.')
	name = toks[0]
	flag = False
	for n in symTableSt[::-1]:
		if name in symTableDict[n].symbols:
			flag = True
			table = symTableDict[n]
			break
	if not flag:
		print('Type of', name, 'not found on line number', lineno)
		return 'Unknown'
	entry = table.get(name)
	if len(toks) == 1:
		return entry.getType()
	fields = entry.getSign()
	field = toks[1]
	if field not in fields:
		return 'Unknown'
	return fields[field][2]

def flatten_list(l):
	output = []
	for i in l:
		if type(i) == list:
			flatten_list(i)
		else:
			output.append(i)
	return output
def p_empty(p):
	'empty :'
	pass

def p_keyword_lcurly(p):
	'''
	keyword_lcurly : LCURLY
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	key = "sym#" + str(p.lexer.lineno) + "#" + str(p.lexer.lexpos)
	symtab = SymbolTable(symTableDict[symTableSt[-1]], key)
	symTableDict[key] = symtab
	symTableSt += [key]
	if (actRecordSt == []):
	  pname = None
	else:
	  pname = actRecordSt[-1]
	actRecord = ActivationRecord(key, pname)
	actRecordDict[key] = actRecord
	actRecordSt += [actRecord.getName()]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'keyword_lcurly')

def p_keyword_rcurly(p):
	'''
	keyword_rcurly : RCURLY
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	sym_table = symTableDict[symTableSt[-1]]
	act_record = actRecordDict[actRecordSt[-1]]
	act_record.setLocalVarsInputArgs(sym_table)
	symTableSt = symTableSt[:-1]
	actRecordSt = actRecordSt[:-1]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'keyword_rcurly')

def p_source_file(p):
	'''
	SourceFile  : PackageClause ImportDeclList TopLevelDeclList
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	for record_name in actRecordDict:
	  if (record_name == "root"):
	    continue
	  actRecordDict[record_name].setGlobalVars(actRecordDict["root"].getGlobalVars())
	  actRecordDict[record_name].setConstVars(actRecordDict["root"].getConstVars())
	p[0]['dict_code'] = p[3]['dict_code']
	print(symTableDict)
	for key in symTableDict:
	    symTableDict[key].prettyPrint()
	print()
	for key in actRecordDict:
	    actRecordDict[key].prettyPrint()
	print()
	p[0]['activationRecords'] = actRecordDict
	for key in p[0]['dict_code']:
	  print(key + ":")
	  for code, scope in zip(p[0]['dict_code'][key][0], p[0]['dict_code'][key][1]):
	    print(code, "           | Scope:", scope)
	  print()
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'SourceFile')

def p_package_clause(p):
	'''
	PackageClause  : PACKAGE IDENTIFIER
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'PackageClause')

def p_import_decl_list(p):
	'''
	ImportDeclList : ImportDecl ImportDeclList
	               | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ImportDeclList')

def p_import_decl(p):
	'''
	ImportDecl    : IMPORT ImportSpecTopList
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ImportDecl')

def p_import_spec_top_list(p):
	'''
	ImportSpecTopList : ImportSpec
	                  | LPAREN ImportSpecList RPAREN
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ImportSpecTopList')

def p_import_spec_list(p):
	'''
	ImportSpecList : ImportSpec ImportSpecList
	               | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ImportSpecList')

def p_import_spec(p):
	'''
	ImportSpec       :  ImportSpecInit ImportPath
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ImportSpec')

def p_import_spec_init(p):
	'''
	ImportSpecInit : DOT
	               | IDENTIFIER
	               | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ImportSpecInit')

def p_import_path(p):
	'''
	ImportPath     : STRINGLIT
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	scope = symTableSt[-1]
	symTable = symTableDict[scope]
	name = p[1].replace('"', '')
	entry = ImportEntry(name)
	if (symTable.put(entry) == False):
	     print("Error:", name, "redeclared on line number", p.lexer.lineno)
	     sys.exit(0)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ImportPath')

def p_top_level_decl_list(p):
	'''
	TopLevelDeclList : TopLevelDecl TopLevelDeclList
	                 | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="TopLevelDeclList" and p.slice[1].type=="TopLevelDecl":
		#p[0]['dict_code'].update(p[1]['dict_code'])
		#p[0]['dict_code'].update(p[2]['dict_code'])
		final_dict_code = {}
		for key in p[1]['dict_code']:
		  if key in p[2]['dict_code']:
		    final_dict_code[key] = (p[1]['dict_code'][key][0] + p[2]['dict_code'][key][0], p[1]['dict_code'][key][1] + p[2]['dict_code'][key][1])
		  else:
		    final_dict_code[key] = (p[1]['dict_code'][key][0], p[1]['dict_code'][key][1])
		for key in p[2]['dict_code']:
		  if not key in p[1]['dict_code']:
		    final_dict_code[key] = (p[2]['dict_code'][key][0], p[2]['dict_code'][key][1])
		p[0]['dict_code'] = final_dict_code
	if len(p)==2 and p.slice[1].type=="empty":
		sym_table = symTableDict[symTableSt[-1]]
		act_record = actRecordDict[actRecordSt[-1]]
		act_record.setLocalVarsInputArgs(sym_table)
		act_record.setGlobalVars(act_record.getLocalVars())
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'TopLevelDeclList')

def p_top_level_decl(p):
	'''
	TopLevelDecl  : Declaration
	              | FunctionDecl
	              | MethodDecl
	              | InterfaceDecl
	              | IFuncDef
	              | StructDef
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="Declaration":
		p[0]['dict_code']['global_decl'] = code_optimization(p[1]['global_decl'], p[1]['scope_global_decl'])
		p[0]['dict_code']['const_decl'] = code_optimization(p[1]['const_decl'], p[1]['scope_const_decl'])
	if len(p)==2 and p.slice[1].type=="FunctionDecl":
		p[0]['dict_code'].update(p[1]['dict_code'])
	if len(p)==2 and p.slice[1].type=="MethodDecl":
		p[0]['dict_code'].update(p[1]['dict_code'])
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'TopLevelDecl')

def p_struct_def(p):
	'''
	StructDef : TYPE IDENTIFIER STRUCT keyword_lcurly ParameterDeclList2 keyword_rcurly
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	scope = symTableSt[-1]
	symTable = symTableDict[scope]
	struc = StructEntry(p[2])
	struc.addFields(p[5]['fields'])
	struc.setSize()
	if (symTable.put(struc) == False):
	     print("Error:", p[2], "redeclared on line number", p.lexer.lineno)
	     sys.exit(0)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'StructDef')

def p_parameter_decl_list2(p):
	'''
	ParameterDeclList2  : ParameterDecl2 ParameterDeclList2
	                    | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="ParameterDeclList2" and p.slice[1].type=="ParameterDecl2":
		p[0]['fields'] = p[1]['fields']
		p[0]['fields'].update(p[2]['fields'])
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['fields'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ParameterDeclList2')

def p_parameter_decl2(p):
	'''
	ParameterDecl2  : IdentifierList1 Type
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="Type" and p.slice[1].type=="IdentifierList1":
		p[0]['fields'] = {}
		for id in p[1]['idlist']:
		  p[0]['fields'][id] = p[2]['type']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ParameterDecl2')

def p_interface_decl(p):
	'''
	InterfaceDecl : TYPE IDENTIFIER INTERFACE interfaceBlock
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	scope = symTableSt[-1]
	symTable = symTableDict[scope]
	interfc = InterfaceEntry(p[2])
	if (symTable.put(interfc) == False):
	    print("Error:", p[2], "redeclared on line number", p.lexer.lineno)
	    sys.exit(0)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'InterfaceDecl')

def p_interface_block(p):
	'''
	interfaceBlock  : keyword_lcurly IFuncDecList keyword_rcurly
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'interfaceBlock')

def p_i_func_dec_list(p):
	'''
	IFuncDecList   : IFuncDec IFuncDecList
	               | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'IFuncDecList')

def p_i_func_dec(p):
	'''
	IFuncDec      : IDENTIFIER LPAREN RPAREN Type
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	scope = symTableSt[-1]
	symTable = symTableDict[scope]
	fn = FuncEntry(p[1])
	if (symTable.put(fn) == False):
	    print("Error:", p[1], "redeclared on line number", p.lexer.lineno)
	    sys.exit(0)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'IFuncDec')

def p_i_func_def(p):
	'''
	IFuncDef      : FUNC LPAREN IDENTIFIER IDENTIFIER RPAREN IFuncDec Block
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'IFuncDef')

def p_block(p):
	'''
	Block : keyword_lcurly StatementList keyword_rcurly
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[2]['code']
	p[0]['scopelist'] = p[2]['scopelist']
	p[0]['ret_typelist'] = p[2]['ret_typelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Block')

def p_statement_list(p):
	'''
	StatementList : Statement StatementList
	              | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['ret_typelist'] = []
	if len(p)==3 and p.slice[2].type=="StatementList" and p.slice[1].type=="Statement":
		p[0]['code'] = p[1]['code'] + p[2]['code']
		p[0]['scopelist'] = p[1]['scopelist'] + p[2]['scopelist']
		p[0]['ret_typelist'] = [p[1]['typelist']] + p[2]['ret_typelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'StatementList')

def p_statement(p):
	'''
	Statement : Declaration
	          | SimpleStmt
	          | ReturnStmt
	          | Block
	          | IfStmt
	          | SwitchStmt
	          | ForStmt
	          | FuncCallStmt
	          | GoFunc
	          | BreakStmt
	          | ContinueStmt
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[1]['code']
	p[0]['scopelist'] = p[1]['scopelist']
	p[0]['typelist'] = []
	if len(p)==2 and p.slice[1].type=="ReturnStmt":
		p[0]['typelist'] = p[1]['typelist']
	if len(p)==2 and p.slice[1].type=="Block":
		for typ in p[1]['ret_typelist']:
		    p[0]['typelist'] += typ
	if len(p)==2 and p.slice[1].type=="IfStmt":
		for typ in p[1]['ret_typelist']:
		    p[0]['typelist'] += typ
	if len(p)==2 and p.slice[1].type=="SwitchStmt":
		for typ in p[1]['ret_typelist']:
		    p[0]['typelist'] += typ
	if len(p)==2 and p.slice[1].type=="GoFunc":
		actRecordSt = actRecordSt[:-1]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Statement')

def p_continue_stmt(p):
	'''
	ContinueStmt : CONTINUE
	             | CONTINUE IDENTIFIER
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="CONTINUE":
		p[0]['code'] = ["goto beglabel"]
		p[0]['scopelist'] =[actRecordSt[-1]]
	if len(p)==3 and p.slice[2].type=="IDENTIFIER" and p.slice[1].type=="CONTINUE":
		p[0]['code'] = ["goto " + p[2]]
		p[0]['scopelist'] = [actRecordSt[-1]]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ContinueStmt')

def p_break_stmt(p):
	'''
	BreakStmt : BREAK
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = ["goto endlabel"]
	p[0]['scopelist'] = [actRecordSt[-1]]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'BreakStmt')

def p_go_func(p):
	'''
	GoFunc    : GO FUNC Parameters FunctionBody LPAREN ExpressionList RPAREN
	          | GO IDENTIFIER LPAREN ExpressionListBot RPAREN
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==8 and p.slice[7].type=="RPAREN" and p.slice[6].type=="ExpressionList" and p.slice[5].type=="LPAREN" and p.slice[4].type=="FunctionBody" and p.slice[3].type=="Parameters" and p.slice[2].type=="FUNC" and p.slice[1].type=="GO":
		code = ["start_go_func:"] + p[6]['code']
		scope = [actRecordSt[-1]] + p[6]['scopelist']
		for id, value in zip(p[3]['idlist'], p[6]['namelist']):
		    code += [id + " := " + value]
		    scope += [actRecordSt[-1]]
		code += p[4]['code']
		p[0]['scopelist'] = scope + p[4]['scopelist']
		p[0]['code'] = code + ["end_go_func"]
		p[0]['scopelist'] += [actRecordSt[-1]]
	if len(p)==6 and p.slice[5].type=="RPAREN" and p.slice[4].type=="ExpressionListBot" and p.slice[3].type=="LPAREN" and p.slice[2].type=="IDENTIFIER" and p.slice[1].type=="GO":
		scope = symTableSt[-1]
		symTable = symTableDict[scope]
		fn = FuncEntry(p[2])
		if (symTable.put(fn) == False):
		    print("Error:", p[2], "redeclared on line number", p.lexer.lineno)
		    sys.exit(0)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'GoFunc')

def p_func_call_stmt(p):
	'''
	FuncCallStmt : IDENTIFIER DOT FuncCallStmt
	             | IDENTIFIER DOT IDENTIFIER LPAREN ExpressionListBot RPAREN
	             | IDENTIFIER LPAREN ExpressionListBot RPAREN
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['ret_types'] = []
	p[0]['namelist'] = []
	#actRecordSt += [actRecordSt[-1]]
	#actRecordSt += ["root"]
	#print(actRecordSt)
	if len(p)==4 and p.slice[3].type=="FuncCallStmt" and p.slice[2].type=="DOT" and p.slice[1].type=="IDENTIFIER":
		b = False
		for scope in symTableSt:
			if p[1] in symTableDict[scope].symbols:
				b = True
				break
		if not b:
		  print("Function", p[1], "not defined on line number", p.lexer.lineno)
		  sys.exit(0)
		p[0]['ret_types'] = p[3]['ret_types']
		p[0]['code'] = p[3]['code']
		p[0]['scopelist'] = p[3]['scopelist']
	if len(p)==7 and p.slice[6].type=="RPAREN" and p.slice[5].type=="ExpressionListBot" and p.slice[4].type=="LPAREN" and p.slice[3].type=="IDENTIFIER" and p.slice[2].type=="DOT" and p.slice[1].type=="IDENTIFIER":
		b = False
		for scope in symTableSt:
			if p[1] in symTableDict[scope].symbols:
				b = True
				break
		if not b:
		  print("Function", p[1], "not defined on line number", p.lexer.lineno)
		  sys.exit(0)
		p[0]['code'] = p[5]['code']
		p[0]['scopelist'] = p[5]['scopelist']
		for name in p[0]['namelist']:
		  p[0]['code'] += ["ret_alloc 4"] # 4 for now
		  p[0]['scopelist'] += [actRecordSt[-1]]
		for param in p[5]['namelist'][::-1]:
		    p[0]['code'] += ["push_param " + param]
		    p[0]['scopelist'] += [actRecordSt[-1]]
		p[0]['code'] += ["call " + p[1] + "." + p[3]]
		p[0]['scopelist'] += [actRecordSt[-1]]
		for name in p[0]['namelist']:
		  p[0]['code'] += ["ret_param " + name]
		  p['scopelist'] += [actRecordSt[-1]]
	if len(p)==5 and p.slice[4].type=="RPAREN" and p.slice[3].type=="ExpressionListBot" and p.slice[2].type=="LPAREN" and p.slice[1].type=="IDENTIFIER":
		b = False
		for scope in symTableSt:
		  if p[1] in symTableDict[scope].symbols:
		    b = True
		    table = symTableDict[scope]
		    break
		if not b:
		  print("Function", p[1], "not defined on line number", p.lexer.lineno)
		  sys.exit(0)
		entry = table.get(p[1])
		p[0]['ret_types'] = entry.getReturnTypes()
		#actRecordSt[-1] = entry.getName()
		for typ in p[0]['ret_types']:
		  p[0]['namelist'] += [newVar()]
		p[0]['code'] = p[3]['code']
		p[0]['scopelist'] = p[3]['scopelist']
		for name in p[0]['namelist']:
		  p[0]['code'] += ["ret_alloc 4"] # 4 for now
		  p[0]['scopelist'] += [actRecordSt[-1]]
		for param in p[3]['namelist'][::-1]:
		    p[0]['code'] += ["push_param " + param]
		    p[0]['scopelist'] += [actRecordSt[-1]]
		p[0]['code'] += ["call " + p[1]]
		p[0]['scopelist'] += [actRecordSt[-1]]
		for name in p[0]['namelist']:
		  p[0]['code'] += ["ret_param " + name]
		  p[0]['scopelist'] += [actRecordSt[-1]]
		if entry.getInputArgs() != p[3]['typelist']:
		   print("Function", p[1], "arguments mismatch at line num", p.lexer.lineno)
		   sys.exit(0)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'FuncCallStmt')

def p_object_method(p):
	'''
	ObjectMethod : IDENTIFIER DOT IDENTIFIER LPAREN ParameterDeclList2 RPAREN
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ObjectMethod')

def p_declaration(p):
	'''
	Declaration : ConstDecl
	            | TypeDecl
	            | VarDecl
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[1]['code']
	p[0]['scopelist'] = p[1]['scopelist']
	p[0]['scope_global_decl'] = []
	p[0]['scope_const_decl'] = []
	p[0]['const_decl'] = []
	p[0]['global_decl'] = []
	if len(p)==2 and p.slice[1].type=="ConstDecl":
		p[0]['const_decl'] = p[1]['code']
		p[0]['scope_const_decl'] = p[1]['scopelist']
	if len(p)==2 and p.slice[1].type=="VarDecl":
		p[0]['global_decl'] = p[1]['code']
		p[0]['scope_global_decl'] = p[1]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Declaration')

def p_const_decl(p):
	'''
	ConstDecl  : CONST ConstSpecTopList
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[2]['code']
	p[0]['scopelist'] = p[2]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ConstDecl')

def p_const_spec_top_list(p):
	'''
	ConstSpecTopList : ConstSpec
	                 | LPAREN ConstSpecList RPAREN
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="ConstSpec":
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
	if len(p)==4 and p.slice[3].type=="RPAREN" and p.slice[2].type=="ConstSpecList" and p.slice[1].type=="LPAREN":
		p[0]['code'] = p[2]['code']
		p[0]['scopelist'] = p[2]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ConstSpecTopList')

def p_const_spec_list(p):
	'''
	ConstSpecList : ConstSpec ConstSpecList
	              | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="ConstSpecList" and p.slice[1].type=="ConstSpec":
		p[0]['code'] = p[1]['code'] + p[2]['code']
		p[0]['scopelist'] = p[1]['scopelist'] + p[2]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ConstSpecList')

def p_const_spec(p):
	'''
	ConstSpec : IdentifierList1 ConstSpecTail
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	scope = symTableSt[-1]
	symTable = symTableDict[scope]
	actRecord = actRecordDict[actRecordSt[-1]]
	if (len(p[1]['idlist']) != len(p[2]['namelist'])):
	  print("Length mismatch on line number", p.lexer.lineno)
	  sys.exit(0)
	p[0]['code'] = p[1]['code'] + p[2]['code']
	p[0]['scopelist'] = p[1]['scopelist'] + p[2]['scopelist']
	for i,j,k in zip(p[1]['idlist'], p[2]['namelist'], p[2]['typelist']):
	    p[0]['code'] += [i + ' := ' + j]
	    p[0]['scopelist'] += [actRecordSt[-1]]
	    actRecord.putConstVar(i)
	    lit = LitEntry(i, k)
	    if (symTable.put(lit) == False):
	      print("Error:", i, "redeclared on line number", p.lexer.lineno)
	      sys.exit(0)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ConstSpec')

def p_const_spec_tail(p):
	'''
	ConstSpecTail : TypeTop EQ ExpressionList
	              | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==4 and p.slice[3].type=="ExpressionList" and p.slice[2].type=="EQ" and p.slice[1].type=="TypeTop":
		p[0]['namelist'] = p[3]['namelist']
		p[0]['typelist'] = p[3]['typelist']
		p[0]['code'] = p[3]['code']
		p[0]['scopelist'] = p[3]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ConstSpecTail')

def p_type_top(p):
	'''
	TypeTop : Type
	        | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'TypeTop')

def p_identifier_list1(p):
	'''
	IdentifierList1 : IDENTIFIER IdentifierBotList1
	                | MULT IDENTIFIER IdentifierBotList1
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="IdentifierBotList1" and p.slice[1].type=="IDENTIFIER":
		p[0]['idlist'] = [p[1]] + p[2]['idlist']
	if len(p)==4 and p.slice[3].type=="IdentifierBotList1" and p.slice[2].type=="IDENTIFIER" and p.slice[1].type=="MULT":
		p[0]['idlist'] = [p[1]+p[2]] + p[3]['idlist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'IdentifierList1')

def p_identifier_bot_list1(p):
	'''
	IdentifierBotList1 :  IdentifierBotList1 COMMA IDENTIFIER
	                  |  IdentifierBotList1 COMMA MULT IDENTIFIER
	                  | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==4 and p.slice[3].type=="IDENTIFIER" and p.slice[2].type=="COMMA" and p.slice[1].type=="IdentifierBotList1":
		p[0]['idlist'] = p[1]['idlist'] + [p[3]]
	if len(p)==5 and p.slice[4].type=="IDENTIFIER" and p.slice[3].type=="MULT" and p.slice[2].type=="COMMA" and p.slice[1].type=="IdentifierBotList1":
		p[0]['idlist'] = p[1]['idlist'] + [p[3]+p[4]]
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['idlist'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'IdentifierBotList1')

def p_identifier_list3(p):
	'''
	IdentifierList3 : IDENTIFIER IdentifierBotList3
	                | MULT IDENTIFIER IdentifierBotList3
	                | IDENTIFIER DOT IDENTIFIER IdentifierBotList3
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="IdentifierBotList3" and p.slice[1].type=="IDENTIFIER":
		p[0]['idlist'] = [p[1]] + p[2]['idlist']
	if len(p)==4 and p.slice[3].type=="IdentifierBotList3" and p.slice[2].type=="IDENTIFIER" and p.slice[1].type=="MULT":
		p[0]['idlist'] = [p[1] + p[2]] + p[3]['idlist']
	if len(p)==5 and p.slice[4].type=="IdentifierBotList3" and p.slice[3].type=="IDENTIFIER" and p.slice[2].type=="DOT" and p.slice[1].type=="IDENTIFIER":
		p[0]['idlist'] = [p[1] + p[2] + p[3]] + p[4]['idlist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'IdentifierList3')

def p_identifier_bot_list3(p):
	'''
	IdentifierBotList3 : IdentifierBotList3 COMMA IDENTIFIER
	                   | IdentifierBotList3 COMMA MULT IDENTIFIER
	                   | IdentifierBotList3 COMMA IDENTIFIER DOT IDENTIFIER 
	                   | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==4 and p.slice[3].type=="IDENTIFIER" and p.slice[2].type=="COMMA" and p.slice[1].type=="IdentifierBotList3":
		p[0]['idlist'] = p[1]['idlist'] + [p[3]]
	if len(p)==5 and p.slice[4].type=="IDENTIFIER" and p.slice[3].type=="MULT" and p.slice[2].type=="COMMA" and p.slice[1].type=="IdentifierBotList3":
		p[0]['idlist'] = p[1]['idlist'] + [p[3] + p[4]]
	if len(p)==6 and p.slice[5].type=="IDENTIFIER" and p.slice[4].type=="DOT" and p.slice[3].type=="IDENTIFIER" and p.slice[2].type=="COMMA" and p.slice[1].type=="IdentifierBotList3":
		p[0]['idlist'] = p[1]['idlist'] + [p[3] + p[4] + p[5]]
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['idlist'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'IdentifierBotList3')

def p_id_or_array_elem_list(p):
	'''
	IdOrArrayElemList : IdOrArrayElem IdOrArrayElemBotList
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['idlist'] = [p[1]['id']] + p[2]['idlist']
	p[0]['idxlists'] = [p[1]['idxlist']] + p[2]['idxlists']
	p[0]['code'] = p[1]['code'] + p[2]['code']
	p[0]['scopelist'] = p[1]['scopelist'] + p[2]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'IdOrArrayElemList')

def p_id_or_array_elem_bot_list(p):
	'''
	IdOrArrayElemBotList : IdOrArrayElemBotList COMMA IdOrArrayElem
	                      | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==4 and p.slice[3].type=="IdOrArrayElem" and p.slice[2].type=="COMMA" and p.slice[1].type=="IdOrArrayElemBotList":
		p[0]['idlist'] = p[1]['idlist'] + [p[3]['id']]
		p[0]['idxlists'] = p[1]['idxlists'] + [p[3]['idxlist']]
		p[0]['code'] = p[1]['code'] + p[3]['code']
		p[0]['scopelist'] = p[1]['scopelist'] + p[3]['scopelist']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['idlist'] = []
		p[0]['idxlists'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'IdOrArrayElemBotList')

def p_id_or_array_elem(p):
	'''
	IdOrArrayElem : IDENTIFIER MoreDims
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['id'] = p[1]
	p[0]['idxlist'] = p[2]['idxlist']
	p[0]['code'] = p[2]['code']
	p[0]['scopelist'] = p[2]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'IdOrArrayElem')

def p_more_dims(p):
	'''
	MoreDims : LSQUARE Expression RSQUARE MoreDims
	           | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==5 and p.slice[4].type=="MoreDims" and p.slice[3].type=="RSQUARE" and p.slice[2].type=="Expression" and p.slice[1].type=="LSQUARE":
		p[0]['idxlist'] = [p[2]['place']] + p[4]['idxlist']
		p[0]['code'] = p[2]['code'] + p[4]['code']
		p[0]['scopelist'] = p[2]['scopelist'] + p[4]['scopelist']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['idxlist']  = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'MoreDims')

def p_expression_list(p):
	'''
	ExpressionList :  Expression ExpressionBotList
	               |  FuncCallStmt ExpressionBotList
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[1]['code'] + p[2]['code']
	p[0]['scopelist'] = p[1]['scopelist'] + p[2]['scopelist']
	if len(p)==3 and p.slice[2].type=="ExpressionBotList" and p.slice[1].type=="Expression":
		p[0]['namelist'] = [p[1]['place']] + p[2]['namelist']
		p[0]['typelist'] = [p[1]['type']] + p[2]['typelist']
	if len(p)==3 and p.slice[2].type=="ExpressionBotList" and p.slice[1].type=="FuncCallStmt":
		p[0]['namelist'] = p[1]['namelist'] + p[2]['namelist']
		p[0]['typelist'] = p[1]['ret_types'] + p[2]['typelist']
		#actRecordSt = actRecordSt[:-1]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ExpressionList')

def p_expression_bot_list(p):
	'''
	ExpressionBotList : ExpressionBotList COMMA Expression
	                  | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==4 and p.slice[3].type=="Expression" and p.slice[2].type=="COMMA" and p.slice[1].type=="ExpressionBotList":
		p[0]['namelist'] = p[1]['namelist'] + [p[3]['place']]
		p[0]['typelist'] = p[1]['typelist'] + [p[3]['type']]
		p[0]['code'] = p[1]['code'] + p[3]['code']
		p[0]['scopelist'] = p[1]['scopelist'] + p[3]['scopelist']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['namelist'] = []
		p[0]['typelist'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ExpressionBotList')

def p_type_decl(p):
	'''
	TypeDecl : TYPE TypeSpecTopList
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'TypeDecl')

def p_type_spec_top_list(p):
	'''
	TypeSpecTopList : TypeSpec
	                | LPAREN TypeSpecList  RPAREN
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'TypeSpecTopList')

def p_type_spec_list(p):
	'''
	TypeSpecList : TypeSpec TypeSpecList SEMICOLON
	             | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'TypeSpecList')

def p_type_spec(p):
	'''
	TypeSpec : AliasDecl
	         | TypeDef
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'TypeSpec')

def p_alias_decl(p):
	'''
	AliasDecl : IDENTIFIER EQ Type
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'AliasDecl')

def p_type_def(p):
	'''
	TypeDef : IDENTIFIER Type
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	print(p[2])
	scope = symTableSt[-1]
	symTable = symTableDict[scope]
	var = VarEntry(p[1])
	var.setDim(p[2]['dim'])
	var.setDimRanges(p[2]['dimrange'])
	if (symTable.put(var) == False):
	    print("Error:", p[1], "redeclared on line number", p.lexer.lineno)
	    sys.exit(0)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'TypeDef')

def p_type(p):
	'''
	Type : TypeName
	     | TypeLit
	     | LPAREN Type RPAREN
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['dim'] = 0
	p[0]['dimrange'] = []
	if len(p)==2 and p.slice[1].type=="TypeName":
		p[0]['type'] = p[1]['type']
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
	if len(p)==2 and p.slice[1].type=="TypeLit":
		p[0]['type'] = p[1]['type']
		p[0]['dim'] = p[1]['dims']
		p[0]['dimrange'] = p[1]['dimrange']
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
	if len(p)==4 and p.slice[3].type=="RPAREN" and p.slice[2].type=="Type" and p.slice[1].type=="LPAREN":
		p[0]['type'] = p[2]['type']
		p[0]['code'] = p[2]['code']
		p[0]['scopelist'] = p[2]['scopelist'] 
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Type')

def p_type_name(p):
	'''
	TypeName  : IDENTIFIER
	          | MULT IDENTIFIER
	          | QualifiedIdent
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="IDENTIFIER":
		p[0]['type'] = p[1]
	if len(p)==3 and p.slice[2].type=="IDENTIFIER" and p.slice[1].type=="MULT":
		p[0]['type'] = "*" + p[2]
	if len(p)==2 and p.slice[1].type=="QualifiedIdent":
		p[0]['type'] = p[1]['type']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'TypeName')

def p_qualified_ident(p):
	'''
	QualifiedIdent : IDENTIFIER DOT IDENTIFIER
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['type'] = verifyCalType(p[3], p.lexer.lineno)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'QualifiedIdent')

def p_type_lit(p):
	'''
	TypeLit  : ArrayType
	         | StructType
	         | FunctionType
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['type'] = p[1]['type']
	p[0]['dimrange'] = []
	p[0]['code'] = p[1]['code']
	p[0]['scopelist'] = p[1]['scopelist']
	if len(p)==2 and p.slice[1].type=="ArrayType":
		p[0]['dims'] = p[1]['dims']
		p[0]['dimrange'] = p[1]['dimrange']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'TypeLit')

def p_array_type(p):
	'''
	ArrayType  : LSQUARE ArrayLength RSQUARE ElementType
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if p[2]['type'] != "int" and p[2]['type'] != '':
	  print("Array index error on line number", p.lexer.lineno)
	  sys.exit(0)
	p[0]['type'] = p[4]['type']
	p[0]['dims'] = 1 + p[4]['dims']
	p[0]['dimrange'] = [p[2]['place']] + p[4]['dimrange']
	p[0]['code'] = p[2]['code'] + p[4]['code']
	p[0]['scopelist'] = p[2]['scopelist'] + p[4]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ArrayType')

def p_array_length(p):
	'''
	ArrayLength : Expression
	            | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="Expression":
		p[0]['type'] = p[1]['type']
		p[0]['place'] = p[1]['place']
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['type'] = ''
		p[0]['place'] = ''
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ArrayLength')

def p_element_type(p):
	'''
	ElementType : Type
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['type'] = p[1]['type']
	p[0]['dims'] = p[1]['dim']
	p[0]['dimrange'] = p[1]['dimrange']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ElementType')

def p_struct_type(p):
	'''
	StructType    : STRUCT keyword_lcurly FieldDeclList keyword_rcurly
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'StructType')

def p_field_decl_list(p):
	'''
	FieldDeclList : FieldDecl FieldDeclList SEMICOLON
	              | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'FieldDeclList')

def p_field_decl(p):
	'''
	FieldDecl  : FieldDeclHead TagTop
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'FieldDecl')

def p_tag_top(p):
	'''
	TagTop : Tag
	       | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'TagTop')

def p_field_decl_head(p):
	'''
	FieldDeclHead : IdentifierList1 Type
	              | EmbeddedField
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'FieldDeclHead')

def p_embedded_field(p):
	'''
	EmbeddedField : starTop TypeName
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'EmbeddedField')

def p_star_top(p):
	'''
	starTop : MULT
	        | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'starTop')

def p_tag(p):
	'''
	Tag : STRINGLIT
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Tag')

def p_function_type(p):
	'''
	FunctionType  : FUNC Signature
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'FunctionType')

def p_result_top(p):
	'''
	ResultTop : Result
	          | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="Result":
		p[0]['ret_types'] = p[1]['ret_types']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['ret_types'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ResultTop')

def p_result(p):
	'''
	Result   : Ret_Types
	         | Type
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="Ret_Types":
		p[0]['ret_types'] = p[1]['ret_types']
	if len(p)==2 and p.slice[1].type=="Type":
		p[0]['ret_types'] = [p[1]['type']]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Result')

def p_ret__types(p):
	'''
	Ret_Types  : LPAREN TypeList RPAREN
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['ret_types'] = p[2]['types']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Ret_Types')

def p_type_list(p):
	'''
	TypeList : Type TypeListBot
	         | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="TypeListBot" and p.slice[1].type=="Type":
		p[0]['types'] = [p[1]['type']] + p[2]['types']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['types'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'TypeList')

def p_type_list_bot(p):
	'''
	TypeListBot : COMMA Type TypeListBot
	          | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==4 and p.slice[3].type=="TypeListBot" and p.slice[2].type=="Type" and p.slice[1].type=="COMMA":
		p[0]['types'] = [p[2]['type']] + p[3]['types']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['types'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'TypeListBot')

def p_parameters(p):
	'''
	Parameters  : LPAREN ParameterListTop RPAREN
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[2]['code']
	p[0]['scopelist'] = p[2]['scopelist']
	p[0]['args_types'] = p[2]['args_types']
	p[0]['idlist'] = p[2]['idlist']
	params = p[2]['idlist']
	scope = symTableSt[-1]
	for param,t,dim,dimrange in zip(params, p[0]['args_types'],p[2]['dims'], p[2]['dimranges']):
	    table = symTableDict[scope]
	    entry = VarEntry(param)
	    entry.setType(t, table)
	    entry.setDim(dim)
	    entry.setDimRanges(dimrange)
	    entry.isNotLocal()
	    decl  = "_decl array " + t + " " + param
	    decl_tail = ""
	    for dr in dimrange:
	        decl_tail += " " + dr
	    decl += decl_tail
	    toks = decl.split()
	    if len(toks) > 4:
	      p[0]['code'] += [decl]
	      p[0]['scopelist'] += [actRecordSt[-1]]
	    if (table.put(entry) == False):
	        print("Error:", param, "redeclared on line number", p.lexer.lineno)
	        sys.exit(0)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Parameters')

def p_parameter_list_top(p):
	'''
	ParameterListTop : ParameterList commaTop
	                 | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="commaTop" and p.slice[1].type=="ParameterList":
		p[0]['args_types'] = p[1]['args_types']
		p[0]['idlist'] = p[1]['idlist']
		p[0]['dims'] = p[1]['dims']
		p[0]['dimranges'] = p[1]['dimranges']
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['args_types'] = []
		p[0]['idlist'] = []
		p[0]['dims'] = []
		p[0]['dimranges'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ParameterListTop')

def p_comma_top(p):
	'''
	commaTop : COMMA
	         | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'commaTop')

def p_parameter_list(p):
	'''
	ParameterList  : ParameterDecl ParameterDeclList
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['args_types'] = [p[1]['type']] + p[2]['args_types']
	p[0]['idlist'] = p[1]['idlist'] + p[2]['idlist']
	p[0]['dims'] = [p[1]['dim']] + p[2]['dims']
	p[0]['dimranges'] = [p[1]['dimrange']] + p[2]['dimranges']
	p[0]['code'] = p[1]['code'] + p[2]['code']
	p[0]['scopelist'] = p[1]['scopelist'] + p[2]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ParameterList')

def p_parameter_decl_list(p):
	'''
	ParameterDeclList : COMMA ParameterDecl ParameterDeclList
	                  | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==4 and p.slice[3].type=="ParameterDeclList" and p.slice[2].type=="ParameterDecl" and p.slice[1].type=="COMMA":
		p[0]['args_types'] = [p[2]['type']] + p[3]['args_types']
		p[0]['idlist'] = p[2]['idlist'] + p[3]['idlist']
		p[0]['dims'] = [p[2]['dim']] + p[3]['dims']
		p[0]['dimranges'] = [p[2]['dimrange']] + p[3]['dimranges']
		p[0]['code'] = p[2]['code'] + p[3]['code']
		p[0]['scopelist'] = p[2]['scopelist'] + p[3]['scopelist']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['args_types'] = []
		p[0]['idlist'] = []
		p[0]['dims'] = []
		p[0]['dimranges'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ParameterDeclList')

def p_parameter_decl(p):
	'''
	ParameterDecl  : ParameterDeclHead tripledotTop Type
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['type'] = p[3]['type']
	p[0]['idlist'] = p[1]['idlist']
	p[0]['dim'] = p[3]['dim']
	p[0]['dimrange'] = p[3]['dimrange']
	p[0]['code'] = p[1]['code'] + p[3]['code']
	p[0]['scopelist'] = p[1]['scopelist'] + p[3]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ParameterDecl')

def p_tripledot_top(p):
	'''
	tripledotTop : DOT_DOT_DOT
	             | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="DOT_DOT_DOT":
		p[0]['symbol'] = '...'
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['symbol'] = ''
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'tripledotTop')

def p_parameter_decl_head(p):
	'''
	ParameterDeclHead : IdentifierList1
	                  | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="IdentifierList1":
		p[0]['idlist'] = p[1]['idlist']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['idlist'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ParameterDeclHead')

def p_var_decl(p):
	'''
	VarDecl : VAR VarSpecTopList
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[2]['code']
	p[0]['scopelist'] = p[2]['scopelist']
	sym_table = symTableDict[symTableSt[-1]]
	var_symbols = sym_table.getVarSymbols()
	var_names = p[2]['idlist']
	for var_name in var_names:
	  if var_name not in var_symbols:
	     print("Error:", var_name, "not found on symbol table at linenum", p.lexer.lineno)
	     sys.exit(0)
	  var_entry = var_symbols[var_name]
	  type = var_entry.getType()
	  if (var_entry.getDim() <= 0):
	    continue
	  dim_ranges = var_entry.getDimRanges()
	  decl_tail = " "
	  for d in range(var_entry.getDim()):
	    decl_tail += " " + dim_ranges[d]
	  decl = "_decl array " + type + " " + var_entry.getName() + decl_tail
	  var_entry.setType(type, sym_table)
	  p[0]['code'] += [decl]
	  p[0]['scopelist'] += [actRecordSt[-1]]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'VarDecl')

def p_var_spec_top_list(p):
	'''
	VarSpecTopList : VarSpec
	               | LPAREN VarSpecList RPAREN
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="VarSpec":
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
		p[0]['idlist'] = p[1]['idlist']
	if len(p)==4 and p.slice[3].type=="RPAREN" and p.slice[2].type=="VarSpecList" and p.slice[1].type=="LPAREN":
		p[0]['code'] = p[2]['code']
		p[0]['scopelist'] = p[2]['scopelist']
		p[0]['idlist'] = p[2]['idlist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'VarSpecTopList')

def p_var_spec_list(p):
	'''
	VarSpecList : VarSpec VarSpecList SEMICOLON
	            | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==4 and p.slice[3].type=="SEMICOLON" and p.slice[2].type=="VarSpecList" and p.slice[1].type=="VarSpec":
		p[0]['code'] = p[1]['code'] + p[2]['code']
		p[0]['scopelist'] = p[1]['scopelist'] + p[2]['scopelist']
		p[0]['idlist'] = p[1]['idlist'] + p[2]['idlist']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['idlist'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'VarSpecList')

def p_var_spec(p):
	'''
	VarSpec  : IdOrArrayElemList VarSpecTail
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	scope = symTableSt[-1]
	symTable = symTableDict[scope]
	if ((p[2]['type_used'] == False) and  len(p[1]['idlist']) != len(p[2]['namelist'])):
	  print("Length mismatch on line number", p.lexer.lineno)
	  sys.exit(0)
	p[0]['code'] = p[1]['code'] + p[2]['code']
	p[0]['scopelist'] = p[1]['scopelist'] + p[2]['scopelist']
	p[0]['idlist'] = p[1]['idlist']
	mylist = p[1]['idlist']
	mytypelist = p[2]['typelist']
	myidxlists = p[1]['idxlists']
	mynamelist = p[2]['namelist']
	#for name, typ in zip(p[1]['idlist'], p[2]['typelist']):
	#    p[0]['code'] += ["_decl " + typ + " " + name]
	for index in range(len(mylist)):
	    i = mylist[index]
	    var = VarEntry(i)
	    var.setDim(len(myidxlists[index]))
	    var.setDimRanges(myidxlists[index])
	    if (index < len(mynamelist)):
	      p[0]['code'] += [i + " := " + mynamelist[index]]
	      p[0]['scopelist'] += [actRecordSt[-1]]
	    if (p[2]['type_used'] == False):
	      var.setType(mytypelist[index], symTable)
	    else:
	      var.setType(p[2]['typelist'][0], symTable)
	    if (symTable.put(var) == False):
	        print("Error:", i, "redeclared on line number", p.lexer.lineno)
	        sys.exit(0)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'VarSpec')

def p_var_spec_tail(p):
	'''
	VarSpecTail : Type VarSpecMid
	            | EQ ExpressionList
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['namelist'] = p[2]['namelist']
	p[0]['code'] = p[2]['code']
	p[0]['scopelist'] = p[2]['scopelist']
	if len(p)==3 and p.slice[2].type=="VarSpecMid" and p.slice[1].type=="Type":
		p[0]['typelist'] = [p[1]['type']]
		p[0]['type_used'] = True
	if len(p)==3 and p.slice[2].type=="ExpressionList" and p.slice[1].type=="EQ":
		p[0]['typelist'] = p[2]['typelist']
		p[0]['type_used'] = False
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'VarSpecTail')

def p_var_spec_mid(p):
	'''
	VarSpecMid : EQ ExpressionList
	           | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="ExpressionList" and p.slice[1].type=="EQ":
		p[0]['namelist'] = p[2]['namelist']
		p[0]['typelist'] = p[2]['typelist']
		p[0]['code'] = p[2]['code']
		p[0]['scopelist'] = p[2]['scopelist']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['namelist'] = []
		p[0]['typelist'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'VarSpecMid')

def p_function_decl(p):
	'''
	FunctionDecl : FUNC Signature FunctionBodyTop
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['scopelist'] = p[2]['scopelist'] + p[3]['scopelist']
	this_func_sym_table = symTableDict[symTableSt[-1]]
	act_record = actRecordDict[actRecordSt[-1]]
	actRecordSt = actRecordSt[:-1]
	symTableSt = symTableSt[:-1]
	input_args = p[2]['input_args']
	ret_types = p[2]['ret_types']
	func_name = p[2]['func_name']
	scope = symTableSt[-1]
	table = symTableDict[scope]
	entry = symTableDict[symTableSt[-1]].get(func_name)
	act_record.setLocalVarsInputArgs(this_func_sym_table)
	#act_record.storeOldStPtr("%rbp")
	act_record.setRetValues(entry)
	p[0]['code'] = p[2]['code'] + p[3]['code']
	p[0]['dict_code'] = { func_name: code_optimization(p[0]['code'], p[0]['scopelist']) }
	p[3]['ret_actual_types'] = flatten_list(p[3]['ret_actual_types'])
	for ret_actual in p[3]['ret_actual_types']:
	      if (len(ret_actual) > 0 and p[2]['ret_types'] != ret_actual):
	           print("Error:", func_name, "return types mismatch on line number", p.lexer.lineno)
	           sys.exit(0)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'FunctionDecl')

def p_signature(p):
	'''
	Signature  : FunctionName Parameters ResultTop
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	func_name = p[1]['func_name']
	p[0]['input_args'] = p[2]['args_types']
	p[0]['ret_types'] = p[3]['ret_types']
	p[0]['func_name'] = func_name
	p[0]['code'] = p[2]['code']
	p[0]['scopelist'] = p[2]['scopelist']
	entry = symTableDict[symTableSt[-2]].get(func_name)
	entry.setInputArgs(p[0]['input_args'])
	entry.setReturnTypes(p[0]['ret_types'])
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Signature')

def p_function_body_top(p):
	'''
	FunctionBodyTop : FunctionBody
	                | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['ret_actual_types'] = []
	if len(p)==2 and p.slice[1].type=="FunctionBody":
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
		p[0]['ret_actual_types'] = p[1]['ret_typelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'FunctionBodyTop')

def p_function_decl_tail(p):
	'''
	FunctionDeclTail : Function
	                 | Signature
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[1]['code']
	p[0]['scopelist'] = p[1]['scopelist']
	p[0]['input_args'] = p[1]['input_args']
	p[0]['ret_types'] = p[1]['ret_types']
	p[0]['ret_actual_types'] = []
	if len(p)==2 and p.slice[1].type=="Function":
		p[0]['ret_actual_types'] = p[1]['ret_actual_types']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'FunctionDeclTail')

def p_function_name(p):
	'''
	FunctionName : IDENTIFIER
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	table = symTableDict[symTableSt[-1]]
	entry = FuncEntry(p[1])
	if (table.put(entry) == False):
	    print("Error:", p[1], "redeclared on line number", p.lexer.lineno)
	    sys.exit(0)
	p[0]['func_name'] = p[1]
	key = "sym#" + str(p.lexer.lineno) + "#" + str(p.lexer.lexpos)
	symtab = SymbolTable(symTableDict[symTableSt[-1]], key)
	symTableDict[key] = symtab
	symTableSt += [key]
	if (actRecordSt == []):
	  pname = None
	else:
	  pname = actRecordSt[-1]
	actRecord = ActivationRecord(p[1], pname)
	actRecordDict[p[1]] = actRecord
	actRecordSt += [actRecord.getName()]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'FunctionName')

def p_function(p):
	'''
	Function  : Signature FunctionBody
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[2]['code']
	p[0]['scopelist'] = p[2]['scopelist']
	p[0]['input_args'] = p[1]['input_args']
	p[0]['ret_types'] = p[1]['ret_types']
	p[0]['ret_actual_types'] = p[2]['ret_typelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Function')

def p_function_body(p):
	'''
	FunctionBody : LCURLY StatementList RCURLY
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[2]['code']
	p[0]['scopelist'] = p[2]['scopelist']
	p[0]['ret_typelist'] = p[2]['ret_typelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'FunctionBody')

def p_method_decl(p):
	'''
	MethodDecl : FUNC Receiver MethodName FunctionDeclTail
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[2]['code'] + p[3]['code'] + p[4]['code']
	p[0]['scopelist'] = p[2]['scopelist'] + p[3]['scopelist'] + p[4]['scopelist']
	p[0]['dict_code'] = { p[3]: code_optimization(p[0]['code'], p[0]['scopelist']) }
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'MethodDecl')

def p_method_name(p):
	'''
	MethodName : IDENTIFIER
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	scope = symTableSt[-1]
	symTable = symTableDict[scope]
	fn = FuncEntry(p[1])
	if (symTable.put(fn) == False):
	    print("Error:", p[1], "redeclared on line number", p.lexer.lineno)
	    sys.exit(0)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'MethodName')

def p_receiver(p):
	'''
	Receiver  : Parameters
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Receiver')

def p_simple_stmt(p):
	'''
	SimpleStmt : ExpressionStmt
	           | Assignment
	           | AssignmentGen
	           | ShortVarDecl
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[1]['code']
	p[0]['scopelist'] = p[1]['scopelist']
	p[0]['place'] = ''
	if len(p)==2 and p.slice[1].type=="ExpressionStmt":
		p[0]['place'] = p[1]['place']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'SimpleStmt')

def p_simple_stmt_bot(p):
	'''
	SimpleStmtBot : SimpleStmt
	           | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="SimpleStmt":
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
		p[0]['place'] = p[1]['place']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['place'] = ""
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'SimpleStmtBot')

def p_expression_stmt(p):
	'''
	ExpressionStmt : Expression
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[1]['code']
	p[0]['scopelist'] = p[1]['scopelist']
	p[0]['place'] = p[1]['place']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ExpressionStmt')

def p_short_var_decl(p):
	'''
	ShortVarDecl : IdentifierList3 SHORT_ASSIGN ExpressionList
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	for name, typ in zip(p[1]['idlist'], p[3]['typelist']):
	    p[0]['code'] += ["_decl " + typ + " " + name]
	    p[0]['scopelist'] += [actRecordSt[-1]]
	scope = symTableSt[-1]
	table = symTableDict[scope]
	p[0]['code'] += p[3]['code']
	p[0]['scopelist'] += p[3]['scopelist']
	if (len(p[1]['idlist']) != len(p[3]['namelist'])):
	   print("Left and right side not equal on line number", p.lexer.lineno)
	   sys.exit(0)
	for i, j, k in zip(p[1]['idlist'], p[3]['namelist'], p[3]['typelist']):
	  p[0]['code'] += [i + ' := ' + j]
	  p[0]['scopelist'] += [actRecordSt[-1]]
	  entry = VarEntry(i)
	  entry.setType(k, table)
	  if (table.put(entry) == False):
	     print("Error:", i, "redeclared on line number", p.lexer.lineno)
	     sys.exit(0)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ShortVarDecl')

def p_assignment(p):
	'''
	Assignment : IdentifierList3 assign_op ExpressionList
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	for id in p[1]['idlist']:
	  id = id.split(".")[0]
	  b = False
	  if id[0] in ['*']:
	     id = id[1:]
	  for scope in symTableSt:
	    if id in symTableDict[scope].symbols:
	      b = True
	      break
	  if not b:
	    print("Error:", id, "not defined on line number", p.lexer.lineno)
	    sys.exit(0)
	p[0]['code'] = p[1]['code'] + p[3]['code']
	p[0]['scopelist'] = p[1]['scopelist'] + p[3]['scopelist']
	if (p[2]['len'] == 1):
	  for i, j, k in zip(p[1]['idlist'], p[3]['namelist'], p[3]['typelist']):
	    q = i
	    if q[0] in ['*']:
	       q = q[1:]
	    left_elem_type = verifyCalType(q, p.lexer.lineno)
	    if i[0] in ['*']:
	       left_elem_type = left_elem_type[1:]
	    if left_elem_type != k:
	      print("Error type mismatch in line " +str(p.lexer.lineno) +". Expected type " +left_elem_type+", got type "+ k)
	      sys.exit(0)
	    p[0]['code'] += [i + ' := ' + j] 
	    p[0]['scopelist'] += [actRecordSt[-1]]
	else:
	  for i, j, k in zip(p[1]['idlist'], p[3]['namelist'], p[3]['typelist']):
	    q = i
	    if q[0] in ['*']:
	       q = q[1:]
	    left_elem_type = verifyCalType(q, p.lexer.lineno)
	    if i[0] in ['*']:
	      left_elem_type = left_elem_type[1:]
	    if left_elem_type != k:
	      print("Error type mismatch in line " +str(p.lexer.lineno) +". Expected type " +left_elem_type+", got type "+ k)
	      sys.exit(0)
	    var = newVar()
	    var_dest = newVar()
	    p[0]['code'] += [var + " := " + i]
	    p[0]['code'] += [var_dest + ' :=  '+ var + " " + p[2]['symbol'] + k + " " + j]
	    p[0]['code'] += [i + " := " + var_dest]
	    p[0]['scopelist'] += [actRecordSt[-1], actRecordSt[-1], actRecordSt[-1]]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Assignment')

def p_assignment_gen(p):
	'''
	AssignmentGen : IdOrArrayElemList assign_op ExpressionList
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[1]['code'] + p[3]['code']
	p[0]['scopelist'] = p[1]['scopelist'] + p[3]['scopelist']
	for i, idx,  j, k in zip(p[1]['idlist'], p[1]['idxlists'],  p[3]['namelist'], p[3]['typelist']):
	  q = i
	  if q[0] in ['*']:
	    q = q[1:]
	  left_elem_type = verifyCalType(q, p.lexer.lineno)
	  if i[0] in ['*']:
	    left_elem_type = left_elem_type[1:]
	  if left_elem_type != k:
	    print("Error type mismatch in line " +str(p.lexer.lineno) +". Expected type " +left_elem_type+", got type "+ k)
	    sys.exit(0)
	  for n in symTableSt[::-1]:
	    if i in symTableDict[n].symbols:
	      table = symTableDict[n]
	  entry = table.get(i)
	  if (entry.getDim() != len(idx)):
	    print("Error: dimention mismatch at line number", p.lexer.lineno)
	    sys.exit(0)
	if (p[2]['len'] == 1):
	    loc = ""
	    for l in idx:
	      loc += "[" + l + "]"
	    p[0]['code'] += [i + loc + ' := ' + j]
	    p[0]['scopelist'] += [actRecordSt[-1]]
	else:
	    p[0]['code'] += [i + ' := ' + i + str(idx) + p2['symbol'] + j]
	    p[0]['scopelist'] += [actRecordSt[-1]]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'AssignmentGen')

def p_assign_op(p):
	'''
	assign_op : addmul_op EQ
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['len'] = 1 + p[1]['len']
	p[0]['symbol'] = p[1]['symbol']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'assign_op')

def p_addmul_op(p):
	'''
	addmul_op : add_op
	          | mul_op
	          | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="add_op":
		p[0]['len'] = 1
		p[0]['symbol'] = p[1]['symbol']
	if len(p)==2 and p.slice[1].type=="mul_op":
		p[0]['len'] = 1
		p[0]['symbol'] = p[1]['symbol']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['len'] = 0
		p[0]['symbol'] = ''
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'addmul_op')

def p_if_stmt(p):
	'''
	IfStmt : IF SimpleStmtBot ExpressionBot Block elseBot
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['lastlabel'] = p[5]['lastlabel']
	p[4]['label'] = newLabel()
	if (p[2]['place'] == ''):
	   print("Inadequate condition at line num", p.lexer.lineno)
	   sys.exit(0)
	if (p[5]['symbol'] != ""):
	   p[0]['code'] = p[2]['code'] + ['if '+ p[2]['place'] + p[3]['symbol'] + ' goto ' + p[4]['label'] + " " +p[5]['symbol']]
	   p[0]['scopelist'] = p[2]['scopelist'] + [actRecordSt[-1]]
	else:
	   p[0]['code'] = p[2]['code'] + ['if '+ p[2]['place'] + p[3]['symbol'] + ' goto ' + p[4]['label'] + " else goto " +p[0]['lastlabel']]
	   p[0]['scopelist'] = p[2]['scopelist'] + [actRecordSt[-1]]
	   
	p[0]['code'] += [p[4]['label'] + ':'] + p[4]['code'] + ["goto " + p[0]['lastlabel']]
	p[0]['scopelist'] += [actRecordSt[-1]] + p[4]['scopelist'] + [actRecordSt[-1]]
	p[0]['code'] += p[5]['code'] + [p[0]['lastlabel'] +": "]
	p[0]['scopelist'] += p[5]['scopelist'] + [actRecordSt[-1]]
	p[0]['ret_typelist'] = p[4]['ret_typelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'IfStmt')

def p_if_stmt2(p):
	'''
	IfStmt2 : IF SimpleStmtBot ExpressionBot Block elseBot
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['lastlabel'] = p[5]['lastlabel']
	p[4]['label'] = newLabel()
	if (p[2]['place'] == ''):
	   print("Inadequate condition at line num", p.lexer.lineno)
	   sys.exit(0)
	if (p[5]['symbol'] != ""):
	   p[0]['code'] = p[2]['code'] + ['if '+ p[2]['place'] + p[3]['symbol'] + ' goto ' + p[4]['label'] + " " +p[5]['symbol']]
	   p[0]['scopelist'] = p[2]['scopelist'] + [actRecordSt[-1]]
	else:
	   p[0]['code'] = p[2]['code'] + ['if '+ p[2]['place'] + p[3]['symbol'] + ' goto ' + p[4]['label'] + " else goto " +p[0]['lastlabel']]
	   p[0]['scopelist'] = p[2]['scopelist'] + [actRecordSt[-1]]
	   
	p[0]['code'] += [p[4]['label'] + ':'] + p[4]['code'] + ["goto " + p[0]['lastlabel']]
	p[0]['scopelist'] += [actRecordSt[-1]] + p[4]['scopelist'] + [actRecordSt[-1]]
	p[0]['code'] += p[5]['code']
	p[0]['scopelist'] += p[5]['scopelist']
	p[0]['ret_typelist'] = p[4]['ret_typelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'IfStmt2')

def p_simple_stmt_bot(p):
	'''
	SimpleStmtBot : SimpleStmt
	              | TRUE
	              | FALSE
	              | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	if len(p)==2 and p.slice[1].type=="SimpleStmt":
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
		p[0]['place'] = p[1]['place']
	if len(p)==2 and p.slice[1].type=="TRUE":
		p[1]['place'] = 'true'
	if len(p)==2 and p.slice[1].type=="FALSE":
		p[0]['place'] = 'false'
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['place'] = ''
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'SimpleStmtBot')

def p_else_bot(p):
	'''
	elseBot : ELSE elseTail
	        | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="elseTail" and p.slice[1].type=="ELSE":
		p[2]['label'] = newLabel()
		p[0]['symbol'] = 'else goto ' + p[2]['label']
		p[0]['code'] = [p[2]['label'] + ' : '] + p[2]['code']
		p[0]['scopelist'] = [actRecordSt[-1]] + p[2]['scopelist']
		p[0]['lastlabel'] = p[2]['lastlabel']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['symbol'] = ''
		p[0]['code'] = []
		p[0]['scopelist'] = []
		p[0]['lastlabel'] = newLabel()
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'elseBot')

def p_else_tail(p):
	'''
	elseTail : IfStmt2
	         | Block
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[1]['code']
	p[0]['scopelist'] = p[1]['scopelist']
	if len(p)==2 and p.slice[1].type=="IfStmt2":
		p[0]['lastlabel'] = p[1]['lastlabel']
	if len(p)==2 and p.slice[1].type=="Block":
		p[0]['lastlabel'] = newLabel()
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'elseTail')

def p_switch_stmt(p):
	'''
	SwitchStmt : ExprSwitchStmt
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['code'] = p[1]['code']
	p[0]['scopelist'] = p[1]['scopelist']
	p[0]['ret_typelist'] = p[1]['ret_typelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'SwitchStmt')

def p_expr_switch_stmt(p):
	'''
	ExprSwitchStmt : SWITCH IDENTIFIER keyword_lcurly ExprCaseClauseList keyword_rcurly
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	b = False
	for scope in symTableSt:
		if p[2] in symTableDict[scope].symbols:
			b = True
			break
	if not b:
	  print("Switch variable", p[2], "not declared on line number", p.lexer.lineno)
	  sys.exit(0)
	p[0]['code'] = p[4]['expcodelist']
	p[0]['scopelist'] = p[4]['expscopelist']
	for exp, label in zip(p[4]['explist'], p[4]['labellist'][:-1]):
	  exp_var = newVar()
	  var = newVar()
	  var2 = newVar()
	  p[0]['code'] += [exp_var + " := " + exp]
	  p[0]['scopelist'] += [actRecordSt[-1]]
	  p[0]['code'] += [var2 + " := " + p[2]]
	  p[0]['scopelist'] += [actRecordSt[-1]]
	  p[0]['code'] += [var + " := " + var2 + ' == ' + exp_var]
	  p[0]['scopelist'] += [actRecordSt[-1]]
	  p[0]['code'] += ['if ' + var + ' goto ' + label]
	  p[0]['scopelist'] += [actRecordSt[-1]]
	for label, codeblock in zip(p[4]['labellist'][:-1], p[4]['code']):
	  p[0]['code'] += codeblock
	  p[0]['scopelist'] += [actRecordSt[-1]]*len(codeblock)
	  p[0]['code'] += ['goto ' + p[4]['labellist'][-1]]
	  p[0]['scopelist'] += [actRecordSt[-1]]
	p[0]['code'] += [p[4]['labellist'][-1] + ':']
	p[0]['scopelist'] += [actRecordSt[-1]]
	p[0]['ret_typelist'] = p[4]['ret_typelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ExprSwitchStmt')

def p_expr_case_clause_list(p):
	'''
	ExprCaseClauseList : ExprCaseClause ExprCaseClauseList
	                   | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="ExprCaseClauseList" and p.slice[1].type=="ExprCaseClause":
		p[0]['explist'] = [p[1]['exp']] + p[2]['explist']
		p[0]['expcodelist'] = p[1]['expcode'] + p[2]['expcodelist']
		p[0]['expscopelist'] = p[1]['expscope'] + p[2]['expscopelist']
		p[0]['labellist'] = [p[1]['label']] + p[2]['labellist']
		p[0]['code'] = [p[1]['code']] + p[2]['code']
		p[0]['scopelist'] = [actRecordSt[-1]] + p[2]['scopelist']
		p[0]['ret_typelist'] = [p[1]['ret_typelist']] + p[2]['ret_typelist']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['explist'] = []
		p[0]['expcodelist'] = []
		p[0]['expscopelist'] = []
		p[0]['labellist'] = [newLabel()]
		p[0]['code'] = []
		p[0]['scopelist'] = []
		p[0]['ret_typelist'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ExprCaseClauseList')

def p_expr_case_clause(p):
	'''
	ExprCaseClause : ExprSwitchCase COLON keyword_lcurly StatementList keyword_rcurly
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['exp'] = p[1]['exp']
	p[0]['expcode'] = p[1]['code']
	p[0]['expscope'] = p[1]['scopelist']
	p[0]['label'] = newLabel()
	p[0]['code'] = [p[0]['label'] + ' : '] + p[4]['code']
	p[0]['scopelist'] = [actRecordSt[-1]] + p[4]['scopelist']
	p[0]['ret_typelist'] = p[4]['ret_typelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ExprCaseClause')

def p_expr_switch_case(p):
	'''
	ExprSwitchCase : CASE Expression
	               | DEFAULT
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="Expression" and p.slice[1].type=="CASE":
		p[0]['exp'] = p[2]['place']
		p[0]['code'] = p[2]['code']
		p[0]['scopelist'] = p[2]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ExprSwitchCase')

def p_for_stmt(p):
	'''
	ForStmt : FOR SimpleStmtBot SEMICOLON SimpleStmtBot SEMICOLON SimpleStmtBot Block
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==8 and p.slice[7].type=="Block" and p.slice[6].type=="SimpleStmtBot" and p.slice[5].type=="SEMICOLON" and p.slice[4].type=="SimpleStmtBot" and p.slice[3].type=="SEMICOLON" and p.slice[2].type=="SimpleStmtBot" and p.slice[1].type=="FOR":
		p[0]['code'] = p[2]['code'] + p[4]['code']
		p[0]['scopelist'] = p[2]['scopelist'] + p[4]['scopelist']
		beglabel = newLabel()
		endlabel = newLabel()
		if (p[4]['place'] != ""):
		  p[0]['code'] += ["if " + p[4]['place'] + " goto " + beglabel + " else goto " + endlabel]
		  p[0]['scopelist'] += [actRecordSt[-1]]
		p[0]['code'] += [beglabel + ":"]
		p[0]['scopelist'] += [actRecordSt[-1]]
		for line in p[7]['code']:
		  if (line == "goto endlabel"):
		    p[0]['code'] += ["goto " + endlabel]
		    p[0]['scopelist'] += [actRecordSt[-1]]
		  elif (line == "goto beglabel"):
		    p[0]['code'] += p[6]['code']
		    p[0]['scopelist'] += p[6]['scopelist']
		    p[0]['code'] += ["goto " + beglabel]
		    p[0]['scopelist'] += [actRecordSt[-1]]
		  else:
		    p[0]['code'] += [line]
		    p[0]['scopelist'] += [actRecordSt[-1]]
		p[0]['code'] += p[6]['code']
		p[0]['scopelist'] += p[6]['scopelist']
		p[0]['code'] += p[4]['code']
		p[0]['scopelist'] += p[4]['scopelist']
		if (p[4]['place'] != ""):
		  p[0]['code'] += ["if " + p[4]['place'] + " goto " + beglabel + " else goto " + endlabel]
		  p[0]['scopelist'] += [actRecordSt[-1]]
		p[0]['code'] += [endlabel + ":"]
		p[0]['scopelist'] += [actRecordSt[-1]]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ForStmt')

def p_expression_bot(p):
	'''
	ExpressionBot : Expression
	              | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="Expression":
		p[0]['symbol'] = p[1]['code'][-1] 
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['symbol'] = ''
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ExpressionBot')

def p_return_stmt(p):
	'''
	ReturnStmt : RETURN ExpressionListBot
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['typelist'] = p[2]['typelist']
	p[0]['code'] = p[2]['code']
	p[0]['scopelist'] = p[2]['scopelist']
	for name in p[2]['namelist']:
	      p[0]['code'] += ["ret " + name]
	      p[0]['scopelist'] += [actRecordSt[-1]]
	p[0]['code'] += ['func_end']
	p[0]['scopelist'] += [actRecordSt[-1]]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ReturnStmt')

def p_expression_list_bot(p):
	'''
	ExpressionListBot : ExpressionList
	                  | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="ExpressionList":
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
		p[0]['typelist'] = p[1]['typelist']
		p[0]['namelist'] = p[1]['namelist']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['typelist'] = []
		p[0]['namelist'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ExpressionListBot')

def p_expression(p):
	'''
	Expression : UnaryExpr
	           | Expression binary_op Expression
	           | IDENTIFIER DOT IDENTIFIER
	           | IDENTIFIER keyword_lcurly ObjectParamList keyword_rcurly
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['type'] = ''
	if len(p)==2 and p.slice[1].type=="UnaryExpr":
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
		p[0]['type'] = p[1]['type']
		p[0]['place'] = p[1]['place']
	if len(p)==4 and p.slice[3].type=="Expression" and p.slice[2].type=="binary_op" and p.slice[1].type=="Expression":
		p[0]['place'] = newVar()
		if p[1]['type'] == p[3]['type']:
		  p[0]['code'] = p[1]['code'] + p[3]['code'] + [p[0]['place'] + ' := ' + p[1]['place'] +" "+ p[2]['symbol'] + p[1]['type']+" " + p[3]['place']]
		  p[0]['scopelist'] = p[1]['scopelist'] + p[3]['scopelist'] + [actRecordSt[-1]]
		  p[0]['type'] = p[1]['type']
		elif (p[1]['type']=='float' and p[3]['type']=='int'):
		  p[0]['code'] = p[1]['code'] + p[3]['code'] + [p[0]['place'] + ' := cast-to-float ' + p[1]['place']+" " + p[2]['symbol'] + 'float ' + p[3]['place']]
		  p[0]['scopelist'] = p[1]['scopelist'] + p[3]['scopelist'] + [actRecordSt[-1]]
		  p[0]['type'] ='float'
		elif (p[3]['type']=='float' and p[1]['type']=='int'):
		  p[0]['code'] = p[1]['code'] + p[3]['code'] + [p[0]['place'] + ' := cast-to-float ' + p[3]['place'] +" "+ p[2]['symbol'] + 'float ' + p[1]['place']]
		  p[0]['scopelist'] = p[1]['scopelist'] + p[3]['scopelist'] + [actRecordSt[-1]]
		  p[0]['type'] ='float'
		elif (p[1]['type']=='string'):
		  p[0]['code'] = p[1]['code'] + p[3]['code'] + [p[0]['place'] + ' := cast-to-string ' + p[3]['place'] +" "+ p[2]['symbol'] + 'string ' + p[1]['place']]
		  p[0]['scopelist'] = p[1]['scopelist'] + p[3]['scopelist'] + [actRecordSt[-1]]
		  p[0]['type'] ='string'
		elif (p[3]['type']=='string'):
		  p[0]['code'] = p[1]['code'] + p[3]['code'] + [p[0]['place'] + ' := cast-to-string ' + p[1]['place'] +" "+ p[2]['symbol'] + 'string ' + p[3]['place']]
		  p[0]['scopelist'] = p[1]['scopelist'] + p[3]['scopelist'] + [actRecordSt[-1]]
		  p[0]['type'] ='string'
	if len(p)==4 and p.slice[3].type=="IDENTIFIER" and p.slice[2].type=="DOT" and p.slice[1].type=="IDENTIFIER":
		p[0]['place'] = newVar()
		p[0]['code'] = [p[0]['place'] + ' := ' + p[1] + '.' + p[3]]
		p[0]['scopelist'] = [actRecordSt[-1]]
		sym_table = symTableDict[symTableSt[-1]]
		symbols = sym_table.getSymbols()
		if p[1] not in symbols:
		   print("Error: type of", p[1], "could not be found on line number", p.lexer.lineno)
		   sys.exit(0)
		var_entry = symbols[p[1]]
		sign = var_entry.getSign()
		typ = sign[p[3]][2]
		p[0]['type'] = typ
	if len(p)==5 and p.slice[4].type=="keyword_rcurly" and p.slice[3].type=="ObjectParamList" and p.slice[2].type=="keyword_lcurly" and p.slice[1].type=="IDENTIFIER":
		p[0]['place'] = newVar()
		p[0]['code'] = p[3]['code']
		p[0]['scopelist'] = p[3]['scopelist']
		p[0]['type'] = p[1]
		p[0]['field_ass'] = p[3]['field_ass']
		code_so_far = p[0]['code'] # Following code is little optimization for saving registers
		scope_so_far = p[0]['scopelist']
		i = 0
		j = 0
		res = []
		resscope = []
		for asgn in p[3]['field_ass']:
		  tmp_name = asgn[1]
		  this_code = p[0]['place'] + "." + asgn[0] + " := " + asgn[1]
		  for j in range(i, len(code_so_far)):
		    if tmp_name in code_so_far[j]:
		      res += [code_so_far[j], this_code]
		      resscope += [scope_so_far[j], actRecordSt[-1]]
		      i = j + 1
		      break
		    else:
		      res += [code_so_far[j]]
		      resscope += [scope_so_far[j]]
		  if (j == len(code_so_far)):
		    res += [this_code]
		    resscope += [actRecordSt[-1]]
		p[0]['code'] = res
		p[0]['scopelist'] = resscope 
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Expression')

def p_object_param_list(p):
	'''
	ObjectParamList : ObjectParam ObjectParamTop
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="ObjectParamTop" and p.slice[1].type=="ObjectParam":
		p[0]['code'] = p[1]['code'] + p[2]['code']
		p[0]['scopelist'] = p[1]['scopelist'] + p[2]['scopelist']
		p[0]['field_ass'] = p[1]['field_ass'] + p[2]['field_ass']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ObjectParamList')

def p_object_param_top(p):
	'''
	ObjectParamTop : COMMA ObjectParamTop
	               | COMMA ObjectParam
	               | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="ObjectParamTop" and p.slice[1].type=="COMMA":
		p[0]['code'] = p[2]['code']
		p[0]['scopelist'] = p[2]['scopelist']
		p[0]['field_ass'] = p[2]['field_ass']
	if len(p)==3 and p.slice[2].type=="ObjectParam" and p.slice[1].type=="COMMA":
		p[0]['code'] = p[2]['code']
		p[0]['scopelist'] = p[2]['scopelist']
		p[0]['field_ass'] = p[2]['field_ass']
	if len(p)==2 and p.slice[1].type=="empty":
		p[0]['code'] = []
		p[0]['scopelist'] = []
		p[0]['field_ass'] = []
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ObjectParamTop')

def p_object_param(p):
	'''
	ObjectParam   : IDENTIFIER COLON Expression
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==4 and p.slice[3].type=="Expression" and p.slice[2].type=="COLON" and p.slice[1].type=="IDENTIFIER":
		p[0]['code'] = p[3]['code']
		p[0]['scopelist'] = p[3]['scopelist']
		p[0]['field_ass'] = [(p[1], p[3]['place'])]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ObjectParam')

def p_unary_expr(p):
	'''
	UnaryExpr  : unary_op UnaryExpr
	           | PrimaryExpr
	           | MULT IDENTIFIER
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==3 and p.slice[2].type=="UnaryExpr" and p.slice[1].type=="unary_op":
		p[0]['place'] = newVar()
		p[0]['type'] = p[2]['type']
		if (p[1]['symbol'] == "&"):
		  p[0]['type'] = "*" + p[0]['type']
		p[0]['code'] = p[2]['code'] + [p[0]['place'] + ' := ' + p[1]['symbol'] + p[2]['place']]
		p[0]['scopelist'] = p[2]['scopelist'] + [actRecordSt[-1]]
	if len(p)==2 and p.slice[1].type=="PrimaryExpr":
		p[0]['place'] = p[1]['place']
		p[0]['type'] = p[1]['type']
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
	if len(p)==3 and p.slice[2].type=="IDENTIFIER" and p.slice[1].type=="MULT":
		p[0]['place'] = newVar()
		p[0]['type'] = verifyCalType(p[2], p.lexer.lineno)[1:]
		p[0]['code'] = [p[0]['place'] + " := " + "*" + p[2]]
		p[0]['scopelist'] = [actRecordSt[-1]]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'UnaryExpr')

def p_binary_op(p):
	'''
	binary_op  : OR_OR
	           | AND_AND
	           | rel_op
	           | add_op
	           | mul_op
	           | MOD
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="OR_OR":
		p[0]['symbol'] = p[1]
	if len(p)==2 and p.slice[1].type=="AND_AND":
		p[0]['symbol'] = p[1]
	if len(p)==2 and p.slice[1].type=="rel_op":
		p[0]['symbol'] = p[1]['symbol']
	if len(p)==2 and p.slice[1].type=="add_op":
		p[0]['symbol'] = p[1]['symbol']
	if len(p)==2 and p.slice[1].type=="mul_op":
		p[0]['symbol'] = p[1]['symbol']
	if len(p)==2 and p.slice[1].type=="MOD":
		p[0]['symbol'] = p[1]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'binary_op')

def p_rel_op(p):
	'''
	rel_op  : EQ_EQ
	        | NOT_EQ
	        | LESS
	        | LESS_EQ
	        | GREATER
	        | GREATER_EQ
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['symbol'] = p[1]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'rel_op')

def p_add_op(p):
	'''
	add_op  : ADD
	        | MINUS
	        | OR
	        | POW
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['symbol'] = p[1]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'add_op')

def p_mul_op(p):
	'''
	mul_op  : MULT
	        | DIV
	        | LSHIFT
	        | RSHIFT
	        | AND
	        | AND_POW
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['symbol'] = p[1]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'mul_op')

def p_unary_op(p):
	'''
	unary_op  : ADD
	          | MINUS
	          | NOT
	          | POW
	          | MULT
	          | AND
	          | RECEIVE
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['symbol'] = p[1]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'unary_op')

def p_primary_expr(p):
	'''
	PrimaryExpr : Operand
	            | PrimaryExpr Selector
	            | PrimaryExpr Index
	            | PrimaryExpr Arguments
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['place'] = newVar()
	if len(p)==2 and p.slice[1].type=="Operand":
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
		p[0]['type'] = p[1]['type']
		p[0]['code'] += [p[0]['place'] + ' := ' + p[1]['place']]
		p[0]['scopelist'] += [actRecordSt[-1]]
	if len(p)==3 and p.slice[2].type=="Selector" and p.slice[1].type=="PrimaryExpr":
		p[0]['code'] = p[1]['code'] + p[2]['code']
		p[0]['scopelist'] = p[1]['scopelist'] + p[2]['scopelist']
		p[0]['code'] += [p[0]['place'] + ' := ' + p[1]['place'] + p[2]['symbol']]
		p[0]['scopelist'] += [actRecordSt[-1]]
	if len(p)==3 and p.slice[2].type=="Index" and p.slice[1].type=="PrimaryExpr":
		p[0]['code'] = p[1]['code'] + p[2]['code']
		p[0]['scopelist'] = p[1]['scopelist'] + p[2]['scopelist']
		p[0]['type'] = p[1]['type']
		p[0]['code'] += [p[0]['place'] + ' := ' + p[1]['place'] + p[2]['symbol']]
		p[0]['scopelist'] += [actRecordSt[-1]]
	if len(p)==3 and p.slice[2].type=="Arguments" and p.slice[1].type=="PrimaryExpr":
		p[0]['code'] = p[1]['code'] + p[2]['code']
		p[0]['scopelist'] = p[1]['scopelist'] + p[2]['scopelist']
		p[0]['type'] = p[1]['type']
		p[0]['code'] += [p[0]['place'] + ' := ' + p[1]['place'] + p[2]['symbol']]
		p[0]['scopelist'] += [actRecordSt[-1]]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'PrimaryExpr')

def p_operand(p):
	'''
	Operand : Literal
	        | OperandName
	        | MethodExpr
	        | LPAREN Expression RPAREN
	        | TRUE
	        | FALSE
	        | FuncCallStmt
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['place'] = newVar()
	if len(p)==2 and p.slice[1].type=="Literal":
		p[0]['code'] = [p[0]['place'] + ' := ' + p[1]['symbol']]
		p[0]['scopelist'] += [actRecordSt[-1]]
		p[0]['type'] = p[1]['type']
	if len(p)==2 and p.slice[1].type=="OperandName":
		p[0]['code'] = p[1]['code'] + [p[0]['place'] + ' := ' + p[1]['place']]
		p[0]['scopelist'] = p[1]['scopelist'] + [actRecordSt[-1]]
		p[0]['type'] = p[1]['type']
	if len(p)==2 and p.slice[1].type=="MethodExpr":
		p[0]['type'] = 'Unknown'
	if len(p)==4 and p.slice[3].type=="RPAREN" and p.slice[2].type=="Expression" and p.slice[1].type=="LPAREN":
		p[0]['type'] = p[2]['type']
		p[0]['code'] = p[2]['code']
		p[0]['scopelist'] = p[2]['scopelist']
		p[0]['code'] += [p[0]['place'] + ' := ' + p[2]['place']]
		p[0]['scopelist'] += [actRecordSt[-1]]
	if len(p)==2 and p.slice[1].type=="TRUE":
		p[0]['code'] = [p[0]['place'] + ' := true']
		p[0]['scopelist'] += [actRecordSt[-1]]
		p[0]['type'] = 'bool'
	if len(p)==2 and p.slice[1].type=="FALSE":
		p[0]['code'] = [p[0]['place'] + ' := false']
		p[0]['scopelist'] += [actRecordSt[-1]]
		p[0]['type'] = 'bool'
	if len(p)==2 and p.slice[1].type=="FuncCallStmt":
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
		p[0]['type'] = ""
		if len(p[1]['ret_types']) > 0:
		  p[0]['type'] = p[1]['ret_types'][0]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Operand')

def p_literal(p):
	'''
	Literal : BasicLit
	        | FunctionLit
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="BasicLit":
		p[0]['type'] = p[1]['type']
		p[0]['symbol'] = p[1]['symbol']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Literal')

def p_basic_lit(p):
	'''
	BasicLit  : INTEGERLIT
	          | FLOATINGLIT
	          | STRINGLIT
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['symbol'] = p[1]
	if len(p)==2 and p.slice[1].type=="INTEGERLIT":
		p[0]['type'] = 'int'
	if len(p)==2 and p.slice[1].type=="FLOATINGLIT":
		p[0]['type'] = 'float'
	if len(p)==2 and p.slice[1].type=="STRINGLIT":
		p[0]['type'] = 'string'
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'BasicLit')

def p_operand_name(p):
	'''
	OperandName : IDENTIFIER
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['place'] = newVar()
	p[0]['code'] = [p[0]['place'] + ' := ' + p[1]]
	#print(actRecordSt)
	p[0]['scopelist'] = [actRecordSt[-1]]
	p[0]['type'] = verifyCalType(p[1], p.lexer.lineno)
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'OperandName')

def p_function_lit(p):
	'''
	FunctionLit : FUNC Function
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'FunctionLit')

def p_method_expr(p):
	'''
	MethodExpr  : ReceiverType DOT MethodName
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'MethodExpr')

def p_receiver_type(p):
	'''
	ReceiverType  : TypeName
	              | LPAREN MULT TypeName RPAREN
	              | LPAREN ReceiverType RPAREN
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ReceiverType')

def p_selector(p):
	'''
	Selector : DOT IDENTIFIER
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['symbol'] = '.' + p[2]
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Selector')

def p_index(p):
	'''
	Index    : LSQUARE Expression RSQUARE
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['symbol'] = '[' + p[2]['place'] + ']'
	p[0]['code'] = p[2]['code']
	p[0]['scopelist'] = p[2]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Index')

def p_arguments(p):
	'''
	Arguments  : LPAREN ArgumentsHead RPAREN
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	p[0]['symbol'] = '(' + p[2]['symbol'] + ')'
	p[0]['code'] = p[2]['code']
	p[0]['scopelist'] = p[2]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'Arguments')

def p_arguments_head(p):
	'''
	ArgumentsHead : ArgumentsHeadMid tripledotTop commaTop
	              | empty
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==4 and p.slice[3].type=="commaTop" and p.slice[2].type=="tripledotTop" and p.slice[1].type=="ArgumentsHeadMid":
		p[0]['symbol'] = p[1]['symbol'] + p[2]['symbol'] +p[3]['symbol']
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ArgumentsHead')

def p_arguments_head_mid(p):
	'''
	ArgumentsHeadMid  : ExpressionList
	                  | Type COMMA ExpressionList
	                  | Type
	'''
	global symTableSt
	global symTableDict
	global actRecordSt
	global actRecordDict
	p[0] = {}
	p[0]['code'] = []
	p[0]['scopelist'] = []
	p[0]['dict_code'] = {}
	if len(p)==2 and p.slice[1].type=="ExpressionList":
		str = ''
		for elt in p[1]['namelist'][:-1]:
		    str += elt + ','
		str += p[1]['namelist'][-1]
		p[0]['symbol'] = str
		p[0]['code'] = p[1]['code']
		p[0]['scopelist'] = p[1]['scopelist']
	if len(p)==4 and p.slice[3].type=="ExpressionList" and p.slice[2].type=="COMMA" and p.slice[1].type=="Type":
		str = p[1]['place'] + ','
		for elt in p[3]['namelist'][:-1]:
		    str += elt + ','
		str += p[3]['namelist'][-1]
		p[0]['symbol'] = str
		p[0]['code'] = p[3]['code']
		p[0]['scopelist'] = p[3]['scopelist']
	if len(p)==2 and p.slice[1].type=="Type":
		p[0]['symbol'] = p[1]['place']
	if len(p[0]['code']) != len(p[0]['scopelist']):
		print(len(p[0]['code']), len(p[0]['scopelist']), 'ArgumentsHeadMid')


def p_error(p):
	print("Parsing error encountered at line number", p.lineno)
	sys.exit(0)

go_parser = yacc.yacc(start="SourceFile")

