import ply.yacc as yacc

from tokrules import tokens

counter = 0

def p_empty(p):
	'empty :'
	pass

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
	PackageClause  : PACKAGE IDENTIFIER
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

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
	StructDef : TYPE IDENTIFIER STRUCT LCURLY ParameterDeclList2 RCURLY
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

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
	InterfaceDecl : TYPE IDENTIFIER INTERFACE interfaceBlock
	'''
	global counter
	p[0] = {"label": "InterfaceDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4]]

def p_interface_block(p):
	'''
	interfaceBlock  : LCURLY IFuncDecList RCURLY
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

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
	IFuncDec      : IDENTIFIER LPAREN RPAREN Type
	'''
	global counter
	p[0] = {"label": "IFuncDec", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4]]

def p_i_func_def(p):
	'''
	IFuncDef      : FUNC LPAREN IDENTIFIER IDENTIFIER RPAREN IFuncDec Block
	'''
	global counter
	p[0] = {"label": "IFuncDef", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3], p[4], p[5], p[6], p[7]]

def p_import_decl(p):
	'''
	ImportDecl    : IMPORT ImportSpecTopList
	'''
	global counter
	p[0] = {"label": "ImportDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_import_spec_top_list(p):
	'''
	ImportSpecTopList : ImportSpec
	                  | LPAREN ImportSpecList RPAREN
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
	ImportSpecInit : DOT
	               | IDENTIFIER
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
	Block : LCURLY StatementList RCURLY
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

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
	GoFunc    : GO FUNC Parameters FunctionBody LPAREN ExpressionList RPAREN
	          | GO IDENTIFIER LPAREN ExpressionListBot RPAREN
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
	FuncCallStmt : IDENTIFIER DOT FuncCallStmt
	             | IDENTIFIER DOT FunctionName LPAREN RPAREN
	             | IDENTIFIER DOT FunctionName LPAREN ExpressionList RPAREN
	             | IDENTIFIER DOT FunctionName LPAREN ObjectMethod RPAREN
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
	ObjectMethod : IDENTIFIER DOT IDENTIFIER LPAREN ParameterDeclList2 RPAREN
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

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
	ConstDecl  : CONST ConstSpecTopList
	'''
	global counter
	p[0] = {"label": "ConstDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_const_spec_top_list(p):
	'''
	ConstSpecTopList : ConstSpec
	                 | LPAREN ConstSpecList RPAREN
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
	ConstSpecTail : TypeTop EQ ExpressionList
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
	IdentifierList : IDENTIFIER IdentifierBotList
	'''
	global counter
	p[0] = {"label": "IdentifierList", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_identifier_bot_list(p):
	'''
	IdentifierBotList :  IdentifierBotList COMMA IDENTIFIER
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
	ExpressionBotList : ExpressionBotList COMMA Expression
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
	TypeDecl : TYPE TypeSpecTopList
	'''
	global counter
	p[0] = {"label": "TypeDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_type_spec_top_list(p):
	'''
	TypeSpecTopList : TypeSpec
	                | LPAREN TypeSpecList  RPAREN
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
	TypeSpecList : TypeSpec TypeSpecList SEMICOLON
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
	AliasDecl : IDENTIFIER EQ Type
	'''
	global counter
	p[0] = {"label": "AliasDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_type_def(p):
	'''
	TypeDef : IDENTIFIER Type
	'''
	global counter
	p[0] = {"label": "TypeDef", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_type(p):
	'''
	Type : TypeName
	     | TypeLit
	     | LPAREN Type RPAREN
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
	TypeName  : IDENTIFIER
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
	QualifiedIdent : IDENTIFIER DOT IDENTIFIER
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

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
	ArrayType  : LSQUARE ArrayLength RSQUARE ElementType
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
	StructType    : STRUCT LCURLY FieldDeclList RCURLY
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_field_decl_list(p):
	'''
	FieldDeclList : FieldDecl FieldDeclList SEMICOLON
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
	starTop : MULT
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
	Tag : STRINGLIT
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_function_type(p):
	'''
	FunctionType  : FUNC Signature
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
	Parameters  : LPAREN ParameterListTop RPAREN
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

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
	commaTop : COMMA
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
	ParameterDeclList : COMMA ParameterDecl ParameterDeclList
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
	tripledotTop : DOT_DOT_DOT
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
	VarDecl : VAR VarSpecTopList
	'''
	global counter
	p[0] = {"label": "VarDecl", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_var_spec_top_list(p):
	'''
	VarSpecTopList : VarSpec
	               | LPAREN VarSpecList RPAREN
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
	VarSpecList : VarSpec VarSpecList SEMICOLON
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
	            | EQ ExpressionList
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
	VarSpecMid : EQ ExpressionList
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
	FunctionDecl : FUNC FunctionName FunctionDeclTail
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
	FunctionName : IDENTIFIER
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

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
	MethodDecl : FUNC Receiver MethodName FunctionDeclTail
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
	ShortVarDecl : IdentifierList SHORT_ASSIGN ExpressionList
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
	assign_op : addmul_op EQ
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

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
	IfStmt : IF SimpleStmtBot ExpressionBot Block elseBot
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
	elseBot : ELSE elseTail
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
	ExprSwitchStmt : SWITCH IDENTIFIER LCURLY ExprCaseClauseList RCURLY
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

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
	ExprCaseClause : ExprSwitchCase COLON LCURLY StatementList RCURLY
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_expr_switch_case(p):
	'''
	ExprSwitchCase : CASE ExpressionList
	               | DEFAULT
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
	ForStmt : FOR ExpressionBot Block
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
	ReturnStmt : RETURN ExpressionListBot
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
	           | IDENTIFIER DOT IDENTIFIER
	           | IDENTIFIER LCURLY ObjectParamList RCURLY
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
	ObjectParamTop : COMMA ObjectParamTop
	               | COMMA ObjectParam
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
	ObjectParam   : IDENTIFIER COLON Expression
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
	binary_op  : OR_OR
	           | AND_AND
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
	rel_op  : EQ_EQ
	        | NOT_EQ
	        | LESS
	        | LESS_EQ
	        | GREATER
	        | GREATER_EQ
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
	add_op  : ADD
	        | MINUS
	        | OR
	        | POW
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
	mul_op  : MULT
	        | DIV
	        | LSHIFT
	        | RSHIFT
	        | AND
	        | AND_POW
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
	unary_op  : ADD
	          | MINUS
	          | NOT
	          | POW
	          | MULT
	          | AND
	          | RECEIVE
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
	        | LPAREN Expression RPAREN
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
	BasicLit  : INTEGERLIT
	          | FLOATINGLIT
	          | STRINGLIT
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
	OperandName : IDENTIFIER
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_function_lit(p):
	'''
	FunctionLit : FUNC Function
	'''
	global counter
	p[0] = {"label": "FunctionLit", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2]]

def p_method_expr(p):
	'''
	MethodExpr  : ReceiverType DOT MethodName
	'''
	global counter
	p[0] = {"label": "MethodExpr", "id": str(counter)}
	counter += 1
	p[0]['children'] = [p[1], p[2], p[3]]

def p_receiver_type(p):
	'''
	ReceiverType  : TypeName
	              | LPAREN MULT TypeName RPAREN
	              | LPAREN ReceiverType RPAREN
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
	Selector : DOT IDENTIFIER
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_index(p):
	'''
	Index    : LSQUARE Expression RSQUARE
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

def p_arguments(p):
	'''
	Arguments  : LPAREN ArgumentsHead RPAREN
	'''
	global counter
	p[0] = {"label" : p[1], "id": str(counter)}
	counter += 1
	p[0]['children'] = []

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
	ArgumentsHeadMid  : ExpressionList
	                  | Type COMMA ExpressionList
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

go_parser = yacc.yacc(start="SourceFile", write_tables=False)

