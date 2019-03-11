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

def p_keyword_lcurly(p):
	'''
	keyword_lcurly : LCURLY
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_rcurly(p):
	'''
	keyword_rcurly : RCURLY
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_const(p):
	'''
	keyword_const : CONST
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_eq(p):
	'''
	op_eq : EQ
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_identifier(p):
	'''
	identifier : IDENTIFIER
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_comma(p):
	'''
	keyword_comma : COMMA
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_type(p):
	'''
	keyword_type : TYPE
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_semicolon(p):
	'''
	keyword_semicolon : SEMICOLON
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_lsquare(p):
	'''
	keyword_lsquare : LSQUARE
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_rsquare(p):
	'''
	keyword_rsquare : RSQUARE
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_struct(p):
	'''
	keyword_struct : STRUCT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_mult(p):
	'''
	op_mult : MULT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_string_lit(p):
	'''
	string_lit : STRINGLIT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_func(p):
	'''
	keyword_func : FUNC
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_dot_dot_dot(p):
	'''
	dot_dot_dot : DOT_DOT_DOT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_var(p):
	'''
	keyword_var : VAR
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_short_assign(p):
	'''
	op_short_assign : SHORT_ASSIGN
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_add(p):
	'''
	op_add : ADD
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_minus(p):
	'''
	op_minus : MINUS
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_or(p):
	'''
	op_or : OR
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_pow(p):
	'''
	op_pow : POW
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_div(p):
	'''
	op_div : DIV
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_mod(p):
	'''
	op_mod : MOD
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_lshift(p):
	'''
	op_lshift : LSHIFT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_rshift(p):
	'''
	op_rshift : RSHIFT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_and(p):
	'''
	op_and : AND
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_and_pow(p):
	'''
	op_and_pow : AND_POW
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_or_or(p):
	'''
	op_or_or : OR_OR
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_and_and(p):
	'''
	op_and_and : AND_AND
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_if(p):
	'''
	keyword_if : IF
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_else(p):
	'''
	keyword_else : ELSE
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_switch(p):
	'''
	keyword_switch : SWITCH
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_colon(p):
	'''
	colon : COLON
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_case(p):
	'''
	keyword_case : CASE
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_default(p):
	'''
	keyword_default : DEFAULT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_for(p):
	'''
	keyword_for : FOR
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_return(p):
	'''
	keyword_return : RETURN
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_eq_eq(p):
	'''
	op_eq_eq : EQ_EQ
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_not_eq(p):
	'''
	op_not_eq : NOT_EQ
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_less(p):
	'''
	op_less : LESS
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_less_eq(p):
	'''
	op_less_eq : LESS_EQ
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_greater(p):
	'''
	op_greater : GREATER
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_greater_eq(p):
	'''
	op_greater_eq : GREATER_EQ
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_not(p):
	'''
	op_not : NOT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_op_receive(p):
	'''
	op_receive : RECEIVE
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_int_lit(p):
	'''
	int_lit : INTEGERLIT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_float_lit(p):
	'''
	float_lit : FLOATINGLIT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_interface(p):
	'''
	keyword_interface : INTERFACE
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_keyword_go(p):
	'''
	keyword_go : GO
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_source_file(p):
	'''
	SourceFile  : PackageClause ImportDeclList TopLevelDeclList
	'''
	global counter
	p[0] = {"label": "SourceFile", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

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
	TopLevelDeclList : TopLevelDecl TopLevelDeclList
	                 | empty
	'''
	global counter
	p[0] = {"label": "TopLevelDeclList", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_top_level_decl(p):
	'''
	TopLevelDecl  : Declaration
	              | FunctionDecl
	              | MethodDecl
	              | InterfaceDecl
	              | IFuncDef
	              | StructDef
	'''
	global counter
	p[0] = {"label": "TopLevelDecl", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_struct_def(p):
	'''
	StructDef : keyword_type identifier keyword_struct keyword_lcurly ParameterDeclList2 keyword_rcurly
	'''
	global counter
	p[0] = {"label": "StructDef", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4], p[5], p[6]]

def p_parameter_decl_list2(p):
	'''
	ParameterDeclList2  : ParameterDecl2 ParameterDeclList2
	                    | empty
	'''
	global counter
	p[0] = {"label": "ParameterDeclList2", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_parameter_decl2(p):
	'''
	ParameterDecl2  : IdentifierList Type
	'''
	global counter
	p[0] = {"label": "ParameterDecl2", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_parameter_dec_list2(p):
	'''
	ParameterDecList2 : ParameterDecl2 ParameterDecList2
	                  | empty
	'''
	global counter
	p[0] = {"label": "ParameterDecList2", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_parameter_decl2(p):
	'''
	ParameterDecl2 : IdentifierList Type
	'''
	global counter
	p[0] = {"label": "ParameterDecl2", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_interface_decl(p):
	'''
	InterfaceDecl : keyword_type identifier keyword_interface interfaceBlock
	'''
	global counter
	p[0] = {"label": "InterfaceDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4]]

def p_interface_block(p):
	'''
	
	interfaceBlock  : keyword_lcurly IFuncDecList keyword_rcurly
	'''
	global counter
	p[0] = {"label": "interfaceBlock", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_i_func_dec_list(p):
	'''
	
	IFuncDecList   : IFuncDec IFuncDecList
	               | empty
	'''
	global counter
	p[0] = {"label": "IFuncDecList", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_i_func_dec(p):
	'''
	
	IFuncDec      : identifier keyword_lparen keyword_rparen Type
	'''
	global counter
	p[0] = {"label": "IFuncDec", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4]]

def p_i_func_def(p):
	'''
	IFuncDef      : keyword_func keyword_lparen identifier identifier keyword_rparen IFuncDec Block
	'''
	global counter
	p[0] = {"label": "IFuncDef", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4], p[5], p[6], p[7]]

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

def p_block(p):
	'''
	Block : keyword_lcurly StatementList keyword_rcurly
	'''
	global counter
	p[0] = {"label": "Block", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_statement_list(p):
	'''
	StatementList : Statement StatementList 
	              | empty
	'''
	global counter
	p[0] = {"label": "StatementList", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

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
	'''
	global counter
	p[0] = {"label": "Statement", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_go_func(p):
	'''
	GoFunc    : keyword_go keyword_func Parameters FunctionBody keyword_lparen ExpressionList keyword_rparen 
	          | keyword_go identifier keyword_lparen ExpressionListBot keyword_rparen
	'''
	global counter
	p[0] = {"label": "GoFunc", "id": str(counter)}
	counter += 1
	if (len(p) == 8):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5], p[6], p[7]]
	else:
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]

def p_func_call_stmt(p):
	'''
	FuncCallStmt : identifier keyword_dot FuncCallStmt 
	             | identifier keyword_dot FunctionName keyword_lparen keyword_rparen
	             | identifier keyword_dot FunctionName keyword_lparen ExpressionList keyword_rparen
	             | identifier keyword_dot FunctionName keyword_lparen ObjectMethod keyword_rparen
	'''
	global counter
	p[0] = {"label": "FuncCallStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	elif (len(p) == 7):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5], p[6]]
	else:
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5], p[6]]

def p_object_method(p):
	'''
	ObjectMethod : identifier keyword_dot identifier keyword_lparen ParameterDeclList2 keyword_rparen
	'''
	global counter
	p[0] = {"label": "ObjectMethod", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4], p[5], p[6]]

def p_declaration(p):
	'''
	Declaration : ConstDecl 
	            | TypeDecl 
		    | VarDecl
	'''
	global counter
	p[0] = {"label": "Declaration", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_const_decl(p):
	'''
	ConstDecl  : keyword_const ConstSpecTopList
	'''
	global counter
	p[0] = {"label": "ConstDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_const_spec_top_list(p):
	'''
	ConstSpecTopList : ConstSpec 
	                 | keyword_lparen ConstSpecList keyword_rparen
	'''
	global counter
	p[0] = {"label": "ConstSpecTopList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1], p[2], p[3]]

def p_const_spec_list(p):
	'''
	ConstSpecList : ConstSpec ConstSpecList 
	              | empty
	'''
	global counter
	p[0] = {"label": "ConstSpecList", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_const_spec(p):
	'''
	ConstSpec : IdentifierList ConstSpecTail
	'''
	global counter
	p[0] = {"label": "ConstSpec", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_const_spec_tail(p):
	'''
	ConstSpecTail : TypeTop op_eq ExpressionList 
	              | empty
	'''
	global counter
	p[0] = {"label": "ConstSpecTail", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	else:
		p[0]['children'] = [p[1]]

def p_type_top(p):
	'''
	TypeTop : Type 
	        | empty
	'''
	global counter
	p[0] = {"label": "TypeTop", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_identifier_list(p):
	'''
	IdentifierList : identifier IdentifierBotList
	'''
	global counter
	p[0] = {"label": "IdentifierList", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_identifier_bot_list(p):
	'''
	IdentifierBotList :  IdentifierBotList keyword_comma identifier   
	                  | empty
	'''
	global counter
	p[0] = {"label": "IdentifierBotList", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	else:
		p[0]['children'] = [p[1]]

def p_expression_list(p):
	'''
	ExpressionList :  Expression ExpressionBotList
	'''
	global counter
	p[0] = {"label": "ExpressionList", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_expression_bot_list(p):
	'''
	ExpressionBotList : ExpressionBotList keyword_comma Expression
	                  | empty
	'''
	global counter
	p[0] = {"label": "ExpressionBotList", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	else:
		p[0]['children'] = [p[1]]

def p_type_decl(p):
	'''
	TypeDecl : keyword_type TypeSpecTopList
	'''
	global counter
	p[0] = {"label": "TypeDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_type_spec_top_list(p):
	'''
	TypeSpecTopList : TypeSpec 
	                | keyword_lparen TypeSpecList  keyword_rparen
	'''
	global counter
	p[0] = {"label": "TypeSpecTopList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1], p[2], p[3]]

def p_type_spec_list(p):
	'''
	TypeSpecList : TypeSpec TypeSpecList keyword_semicolon 
	             | empty
	'''
	global counter
	p[0] = {"label": "TypeSpecList", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	else:
		p[0]['children'] = [p[1]]

def p_type_spec(p):
	'''
	TypeSpec : AliasDecl 
	         | TypeDef
	'''
	global counter
	p[0] = {"label": "TypeSpec", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_alias_decl(p):
	'''
	AliasDecl : identifier op_eq Type
	'''
	global counter
	p[0] = {"label": "AliasDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_type_def(p):
	'''
	TypeDef : identifier Type
	'''
	global counter
	p[0] = {"label": "TypeDef", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_type(p):
	'''
	Type : TypeName 
	     | TypeLit 
		 | keyword_lparen Type keyword_rparen
	'''
	global counter
	p[0] = {"label": "Type", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1], p[2], p[3]]

def p_type_name(p):
	'''
	TypeName  : identifier 
	          | QualifiedIdent
	'''
	global counter
	p[0] = {"label": "TypeName", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_qualified_ident(p):
	'''
	QualifiedIdent : identifier keyword_dot identifier
	'''
	global counter
	p[0] = {"label": "QualifiedIdent", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_type_lit(p):
	'''
	TypeLit  : ArrayType 
	         | StructType 
			 | FunctionType
	'''
	global counter
	p[0] = {"label": "TypeLit", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_array_type(p):
	'''
	ArrayType  : keyword_lsquare ArrayLength keyword_rsquare ElementType
	'''
	global counter
	p[0] = {"label": "ArrayType", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4]]

def p_array_length(p):
	'''
	
	ArrayLength : Expression
		    | empty
	'''
	global counter
	p[0] = {"label": "ArrayLength", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_element_type(p):
	'''
	
	ElementType : Type
	'''
	global counter
	p[0] = {"label": "ElementType", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1]]

def p_struct_type(p):
	'''
	StructType    : keyword_struct keyword_lcurly FieldDeclList keyword_rcurly
	'''
	global counter
	p[0] = {"label": "StructType", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4]]

def p_field_decl_list(p):
	'''
	FieldDeclList : FieldDecl FieldDeclList keyword_semicolon 
	              | empty
	'''
	global counter
	p[0] = {"label": "FieldDeclList", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	else:
		p[0]['children'] = [p[1]]

def p_field_decl(p):
	'''
	FieldDecl  : FieldDeclHead TagTop
	'''
	global counter
	p[0] = {"label": "FieldDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_tag_top(p):
	'''
	TagTop : Tag 
	       | empty
	'''
	global counter
	p[0] = {"label": "TagTop", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_field_decl_head(p):
	'''
	FieldDeclHead : IdentifierList Type 
	              | EmbeddedField
	'''
	global counter
	p[0] = {"label": "FieldDeclHead", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_embedded_field(p):
	'''
	EmbeddedField : starTop TypeName
	'''
	global counter
	p[0] = {"label": "EmbeddedField", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_star_top(p):
	'''
	starTop : op_mult 
	        | empty
	'''
	global counter
	p[0] = {"label": "starTop", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_tag(p):
	'''
	Tag : string_lit
	'''
	global counter
	p[0] = {"label": "Tag", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1]]

def p_function_type(p):
	'''
	FunctionType  : keyword_func Signature
	'''
	global counter
	p[0] = {"label": "FunctionType", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_signature(p):
	'''
	Signature  : Parameters ResultTop
	'''
	global counter
	p[0] = {"label": "Signature", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_result_top(p):
	'''
	ResultTop : Result 
	          | empty
	'''
	global counter
	p[0] = {"label": "ResultTop", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_result(p):
	'''
	Result   : Parameters 
	         | Type
	'''
	global counter
	p[0] = {"label": "Result", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_parameters(p):
	'''
	Parameters  : keyword_lparen ParameterListTop keyword_rparen
	'''
	global counter
	p[0] = {"label": "Parameters", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_parameter_list_top(p):
	'''
	ParameterListTop : ParameterList commaTop 
	                 | empty
	'''
	global counter
	p[0] = {"label": "ParameterListTop", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_comma_top(p):
	'''
	commaTop : keyword_comma 
	         | empty
	'''
	global counter
	p[0] = {"label": "commaTop", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_parameter_list(p):
	'''
	ParameterList  : ParameterDecl ParameterDeclList
	'''
	global counter
	p[0] = {"label": "ParameterList", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_parameter_decl_list(p):
	'''
	ParameterDeclList : keyword_comma ParameterDecl ParameterDeclList 
	                  | empty
	'''
	global counter
	p[0] = {"label": "ParameterDeclList", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	else:
		p[0]['children'] = [p[1]]

def p_parameter_decl(p):
	'''
	ParameterDecl  : ParameterDeclHead tripledotTop Type
	'''
	global counter
	p[0] = {"label": "ParameterDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_tripledot_top(p):
	'''
	tripledotTop : dot_dot_dot 
	             | empty
	'''
	global counter
	p[0] = {"label": "tripledotTop", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_parameter_decl_head(p):
	'''
	ParameterDeclHead : IdentifierList 
	                  | empty
	'''
	global counter
	p[0] = {"label": "ParameterDeclHead", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_var_decl(p):
	'''
	VarDecl : keyword_var VarSpecTopList
	'''
	global counter
	p[0] = {"label": "VarDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_var_spec_top_list(p):
	'''
	VarSpecTopList : VarSpec 
	               | keyword_lparen VarSpecList keyword_rparen
	'''
	global counter
	p[0] = {"label": "VarSpecTopList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1], p[2], p[3]]

def p_var_spec_list(p):
	'''
	VarSpecList : VarSpec VarSpecList keyword_semicolon 
	            | empty
	'''
	global counter
	p[0] = {"label": "VarSpecList", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	else:
		p[0]['children'] = [p[1]]

def p_var_spec(p):
	'''
	VarSpec  : IdentifierList VarSpecTail
	'''
	global counter
	p[0] = {"label": "VarSpec", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_var_spec_tail(p):
	'''
	VarSpecTail : Type VarSpecMid 
	            | op_eq ExpressionList
	'''
	global counter
	p[0] = {"label": "VarSpecTail", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1], p[2]]

def p_var_spec_mid(p):
	'''
	VarSpecMid : op_eq ExpressionList 
	           | empty
	'''
	global counter
	p[0] = {"label": "VarSpecMid", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_function_decl(p):
	'''
	FunctionDecl : keyword_func FunctionName FunctionDeclTail
	'''
	global counter
	p[0] = {"label": "FunctionDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_function_decl_tail(p):
	'''
	FunctionDeclTail : Function 
	                 | Signature
	'''
	global counter
	p[0] = {"label": "FunctionDeclTail", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_function_name(p):
	'''
	FunctionName : identifier
	'''
	global counter
	p[0] = {"label": "FunctionName", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1]]

def p_function(p):
	'''
	Function  : Signature FunctionBody
	'''
	global counter
	p[0] = {"label": "Function", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_function_body(p):
	'''
	FunctionBody : Block 
	'''
	global counter
	p[0] = {"label": "FunctionBody", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1]]

def p_method_decl(p):
	'''
	MethodDecl : keyword_func Receiver MethodName FunctionDeclTail
	'''
	global counter
	p[0] = {"label": "MethodDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4]]

def p_method_name(p):
	'''
	MethodName : IDENTIFIER
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_receiver(p):
	'''
	Receiver  : Parameters
	'''
	global counter
	p[0] = {"label": "Receiver", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1]]

def p_simple_stmt(p):
	'''
	SimpleStmt : ExpressionStmt 
	           | Assignment 
			   | ShortVarDecl
	'''
	global counter
	p[0] = {"label": "SimpleStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_expression_stmt(p):
	'''
	ExpressionStmt : Expression
	'''
	global counter
	p[0] = {"label": "ExpressionStmt", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1]]

def p_short_var_decl(p):
	'''
	 
	ShortVarDecl : IdentifierList op_short_assign ExpressionList 
	'''
	global counter
	p[0] = {"label": "ShortVarDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_assignment(p):
	'''
	Assignment : ExpressionList assign_op ExpressionList
	'''
	global counter
	p[0] = {"label": "Assignment", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_assign_op(p):
	'''
	assign_op : addmul_op op_eq
	'''
	global counter
	p[0] = {"label": "assign_op", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_addmul_op(p):
	'''
	addmul_op : add_op 
	          | mul_op 
			  | empty
	'''
	global counter
	p[0] = {"label": "addmul_op", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_if_stmt(p):
	'''
	IfStmt : keyword_if SimpleStmtBot ExpressionBot Block elseBot
	'''
	global counter
	p[0] = {"label": "IfStmt", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]

def p_simple_stmt_bot(p):
	'''
	SimpleStmtBot : SimpleStmt 
	              | TRUE
	              | FALSE
	              | empty
	'''
	global counter
	p[0] = {"label": "SimpleStmtBot", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_else_bot(p):
	'''
	elseBot : keyword_else elseTail 
	        | empty
	'''
	global counter
	p[0] = {"label": "elseBot", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_else_tail(p):
	'''
	elseTail : IfStmt 
	         | Block
	'''
	global counter
	p[0] = {"label": "elseTail", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_switch_stmt(p):
	'''
	SwitchStmt : ExprSwitchStmt
	'''
	global counter
	p[0] = {"label": "SwitchStmt", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1]]

def p_expr_switch_stmt(p):
	'''
	ExprSwitchStmt : keyword_switch identifier keyword_lcurly ExprCaseClauseList keyword_rcurly
	'''
	global counter
	p[0] = {"label": "ExprSwitchStmt", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]

def p_expr_case_clause_list(p):
	'''
	ExprCaseClauseList : ExprCaseClause ExprCaseClauseList 
	                   | empty
	'''
	global counter
	p[0] = {"label": "ExprCaseClauseList", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_expr_case_clause(p):
	'''
	ExprCaseClause : ExprSwitchCase colon keyword_lcurly StatementList keyword_rcurly
	'''
	global counter
	p[0] = {"label": "ExprCaseClause", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]

def p_expr_switch_case(p):
	'''
	ExprSwitchCase : keyword_case ExpressionList 
	               | keyword_default
	'''
	global counter
	p[0] = {"label": "ExprSwitchCase", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_for_stmt(p):
	'''
	ForStmt : keyword_for ExpressionBot Block
	'''
	global counter
	p[0] = {"label": "ForStmt", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_expression_bot(p):
	'''
	ExpressionBot : Expression 
	              | empty
	'''
	global counter
	p[0] = {"label": "ExpressionBot", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_return_stmt(p):
	'''
	ReturnStmt : keyword_return ExpressionListBot
	'''
	global counter
	p[0] = {"label": "ReturnStmt", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_expression_list_bot(p):
	'''
	ExpressionListBot : ExpressionList 
	                  | empty
	'''
	global counter
	p[0] = {"label": "ExpressionListBot", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_expression(p):
	'''
	Expression : UnaryExpr 
	           | Expression binary_op Expression
	           | identifier keyword_dot identifier
	           | identifier keyword_lcurly ObjectParamList keyword_rcurly
	'''
	global counter
	p[0] = {"label": "Expression", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	else:
		p[0]['children'] = [p[1], p[2], p[3], p[4]]

def p_object_param_list(p):
	'''
	ObjectParamList : ObjectParam ObjectParamTop
	'''
	global counter
	p[0] = {"label": "ObjectParamList", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_object_param_top(p):
	'''
	ObjectParamTop : keyword_comma ObjectParamTop
	               | keyword_comma ObjectParam
	               | empty
	'''
	global counter
	p[0] = {"label": "ObjectParamTop", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1]]

def p_object_param(p):
	'''
	ObjectParam   : identifier colon Expression
	'''
	global counter
	p[0] = {"label": "ObjectParam", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_unary_expr(p):
	'''
	UnaryExpr  : PrimaryExpr 
	           | unary_op UnaryExpr
	'''
	global counter
	p[0] = {"label": "UnaryExpr", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1], p[2]]

def p_binary_op(p):
	'''
	binary_op  : op_or_or 
	           | op_and_and 
			   | rel_op 
			   | add_op 
			   | mul_op
	'''
	global counter
	p[0] = {"label": "binary_op", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_rel_op(p):
	'''
	rel_op  : op_eq_eq 
	        | op_not_eq 
			| op_less 
			| op_less_eq 
			| op_greater 
			| op_greater_eq
	'''
	global counter
	p[0] = {"label": "rel_op", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_add_op(p):
	'''
	add_op  : op_add 
	        | op_minus 
			| op_or 
			| op_pow
	'''
	global counter
	p[0] = {"label": "add_op", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_mul_op(p):
	'''
	mul_op  : op_mult 
	        | op_div 
	        | op_lshift 
	        | op_rshift 
	        | op_and 
	        | op_and_pow
	'''
	global counter
	p[0] = {"label": "mul_op", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_unary_op(p):
	'''
	unary_op : op_add 
	        | op_minus 
			| op_not 
			| op_pow 
			| op_mult 
			| op_and 
			| op_receive
	'''
	global counter
	p[0] = {"label": "unary_op", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_primary_expr(p):
	'''
	PrimaryExpr : Operand
	            | PrimaryExpr Selector
	            | PrimaryExpr Index
	            | PrimaryExpr Arguments
	'''
	global counter
	p[0] = {"label": "PrimaryExpr", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	else:
		p[0]['children'] = [p[1], p[2]]

def p_operand(p):
	'''
	Operand : Literal 
	        | OperandName 
	        | MethodExpr 
	        | keyword_lparen Expression keyword_rparen
	        | TRUE
	        | FALSE
	'''
	global counter
	p[0] = {"label": "Operand", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_literal(p):
	'''
	Literal : BasicLit 
	        | FunctionLit
	'''
	global counter
	p[0] = {"label": "Literal", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_basic_lit(p):
	'''
	BasicLit : int_lit 
	        | float_lit 
		| string_lit
	'''
	global counter
	p[0] = {"label": "BasicLit", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	else:
		p[0]['children'] = [p[1]]

def p_operand_name(p):
	'''
	OperandName : identifier
	'''
	global counter
	p[0] = {"label": "OperandName", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1]]

def p_function_lit(p):
	'''
	FunctionLit : keyword_func Function
	'''
	global counter
	p[0] = {"label": "FunctionLit", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_method_expr(p):
	'''
	MethodExpr  : ReceiverType keyword_dot MethodName
	'''
	global counter
	p[0] = {"label": "MethodExpr", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_receiver_type(p):
	'''
	ReceiverType : TypeName 
	            | keyword_lparen op_mult TypeName keyword_rparen 
		    | keyword_lparen ReceiverType keyword_rparen
	'''
	global counter
	p[0] = {"label": "ReceiverType", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	else:
		p[0]['children'] = [p[1], p[2], p[3]]

def p_selector(p):
	'''
	Selector : keyword_dot identifier
	'''
	global counter
	p[0] = {"label": "Selector", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_index(p):
	'''
	Index    : keyword_lsquare Expression keyword_rsquare
	'''
	global counter
	p[0] = {"label": "Index", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_arguments(p):
	'''
	Arguments  : keyword_lparen ArgumentsHead keyword_rparen
	'''
	global counter
	p[0] = {"label": "Arguments", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_arguments_head(p):
	'''
	ArgumentsHead : ArgumentsHeadMid tripledotTop commaTop 
	              | empty
	'''
	global counter
	p[0] = {"label": "ArgumentsHead", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	else:
		p[0]['children'] = [p[1]]

def p_arguments_head_mid(p):
	'''
	ArgumentsHeadMid : ExpressionList 
	                 | Type keyword_comma ExpressionList 
			 | Type
	
	'''
	global counter
	p[0] = {"label": "ArgumentsHeadMid", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	else:
		p[0]['children'] = [p[1]]


def p_error(p):
	print("Error encountered at line number", p.lineno)

go_parser = yacc.yacc(start="SourceFile")

