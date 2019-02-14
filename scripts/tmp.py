import ply.yacc as yacc

from tokrules import tokens

counter = 0

def p_start(p):
	'''
	Start     : PackageClause stmt_end ImportDeclList TopLevelDeclList
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Start", "id": str(counter)}
	counter += 1
	if (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_package_clause(p):
	'''
	PackageClause  : keyword_package PackageName
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "PackageClause", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_package_name(p):
	'''
	PackageName    : identifier
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "PackageName", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_import_path(p):
	'''
	ImportPath     : string_literal
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ImportPath", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_import_spec(p):
	'''
	ImportSpec     : ImportPath
	               | dot ImportPath
	               | PackageName ImportPath
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ImportSpec", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_import_list(p):
	'''
	ImportList     : empty
	               | ImportList ImportSpec stmt_end
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ImportList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_import_decl(p):
	'''
	ImportDecl     : keyword_import ImportSpec
	               | keyword_import left_paren ImportList right_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ImportDecl", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_import_decl_list(p):
	'''
	ImportDeclList : empty
	               | ImportDeclList ImportDecl stmt_end
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ImportDeclList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_top_level_decl_list(p):
	'''
	TopLevelDeclList : empty
	                 | TopLevelDeclList TopLevelDecl stmt_end
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "TopLevelDeclList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_top_level_decl(p):
	'''
	TopLevelDecl : Declaration
	             | FunctionDecl
	             | MethodDecl
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
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
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_function_decl(p):
	'''
	FunctionDecl : keyword_func FunctionName Function
	             | keyword_func FunctionName Signature
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "FunctionDecl", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_function_name(p):
	'''
	FunctionName : identifier
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "FunctionName", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_method_decl(p):
	'''
	MethodDecl : keyword_func Receiver MethodName Function
	           | keyword_func Receiver MethodName Signature
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "MethodDecl", "id": str(counter)}
	counter += 1
	if (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_receiver(p):
	'''
	Receiver : Parameters
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Receiver", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_declaration(p):
	'''
	Declaration : ConstDecl
	            | TypeDecl
	            | VarDecl
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Declaration", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_const_decl(p):
	'''
	ConstDecl : keyword_const ConstGroup
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ConstDecl", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_const_group(p):
	'''
	ConstGroup : ConstSpec
	           | left_paren ConstSpecList right_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ConstGroup", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_const_spec_list(p):
	'''
	ConstSpecList : empty
	              | ConstSpecList ConstSpec stmt_end
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ConstSpecList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_const_spec(p):
	'''
	ConstSpec : IdentifierList Type '=' IdentifierList
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ConstSpec", "id": str(counter)}
	counter += 1
	if (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_identifier_list(p):
	'''
	IdentifierList : identifier
	               | IdentifierList comma identifier
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "IdentifierList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_type_decl(p):
	'''
	TypeDecl  : keyword_type TypeSpecGroup
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "TypeDecl", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_type_spec_group(p):
	'''
	TypeSpecGroup : TypeSpec
	              | left_paren TypeSpecList right_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "TypeSpecGroup", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_type_spec_list(p):
	'''
	TypeSpecList : empty
	             | TypeSpecList TypeSpec stmt_end
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "TypeSpecList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_type_spec(p):
	'''
	TypeSpec     : AliasDecl
	             | TypeDef
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "TypeSpec", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_alias_decl(p):
	'''
	AliasDecl    : identifier '=' Type
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "AliasDecl", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_type_def(p):
	'''
	TypeDef      : identifier Type
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "TypeDef", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_type(p):
	'''
	Type      : TypeName
	          | TypeLit
	          | left_paren Type right_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Type", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_type_name(p):
	'''
	TypeName  : identifier
	          | QualifiedIdent
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "TypeName", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_type_lit(p):
	'''
	TypeLit   : ArrayType
	          | StructType
	          | PointerType
	          | FunctionType
	          | InterfaceType
	          | SliceType
	          | MapType
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "TypeLit", "id": str(counter)}
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
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_array_type(p):
	'''
	ArrayType   : left_sq_paren ArrayLength right_sq_paren ElementType
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ArrayType", "id": str(counter)}
	counter += 1
	if (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_array_length(p):
	'''
	ArrayLength : Expression
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ArrayLength", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_element_type(p):
	'''
	ElementType : Type
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ElementType", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_slice_type(p):
	'''
	SliceType : left_sq_paren right_sq_paren ElementType
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "SliceType", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_struct_type(p):
	'''
	StructType    : keyword_struct left_block_bracket FieldDeclList right_block_bracket
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "StructType", "id": str(counter)}
	counter += 1
	if (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_field_decl_list(p):
	'''
	FieldDeclList : empty
	              | FieldDeclList FieldDecl stmt_end
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "FieldDeclList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_field_decl(p):
	'''
	FieldDecl     : IdentifierList Type
	              | EmbeddedField
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "FieldDecl", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_embedded_field(p):
	'''
	EmbeddedField : '*' TypeName
	              | TypeName
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "EmbeddedField", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_pointer_type(p):
	'''
	PointerType : '*' BaseType
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "PointerType", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_base_type(p):
	'''
	BaseType    : Type
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "BaseType", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_function_type(p):
	'''
	FunctionType   : keyword_func Signature
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "FunctionType", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_signature(p):
	'''
	Signature      : Parameters ParametersList Result
	               | Parameters ParametersList
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Signature", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_parameters_list(p):
	'''
	ParametersList : empty
	               | ParametersList Parameters
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ParametersList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_result(p):
	'''
	Result         : Type
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Result", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_parameters(p):
	'''
	Parameters     : left_paren ParameterList comma right_paren
	               | left_paren ParameterList right_paren
	               | left_paren right_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Parameters", "id": str(counter)}
	counter += 1
	if (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_parameter_list(p):
	'''
	ParameterList  : ParameterDecl
	               | ParameterList comma ParameterDecl
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ParameterList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_parameter_decl(p):
	'''
	ParameterDecl  : Type
	               | spread_op Type
	               | IdentifierList Type
	               | IdentifierList spread_op Type
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ParameterDecl", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_interface_type(p):
	'''
	InterfaceType      : keyword_interface left_block_bracket MethodSpecList right_block_bracket
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "InterfaceType", "id": str(counter)}
	counter += 1
	if (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_method_spec_list(p):
	'''
	MethodSpecList : empty
	               | MethodSpecList MethodSpec stmt_end
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "MethodSpecList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_method_spec(p):
	'''
	MethodSpec         : MethodName Signature
	                   | InterfaceTypeName
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "MethodSpec", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_method_name(p):
	'''
	MethodName         : identifier
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "MethodName", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_interface_type_name(p):
	'''
	InterfaceTypeName  : TypeName
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "InterfaceTypeName", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_map_type(p):
	'''
	MapType     : keyword_map left_sq_paren KeyType right_sq_paren ElementType
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "MapType", "id": str(counter)}
	counter += 1
	if (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_key_type(p):
	'''
	KeyType     : Type
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "KeyType", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_qualified_ident(p):
	'''
	QualifiedIdent : PackageName dot identifier
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "QualifiedIdent", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_var_decl(p):
	'''
	VarDecl     : keyword_var VarSpec
	            | keyword_var left_paren VarSpecList right_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "VarDecl", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_var_spec_list(p):
	'''
	VarSpecList : empty
	            | VarSpecList VarSpec stmt_end
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "VarSpecList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_var_spec(p):
	'''
	VarSpec     : IdentifierList ExpressionListGroup
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "VarSpec", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_expression_list_group(p):
	'''
	ExpressionListGroup : Type
	                    | Type '=' ExpressionList
	                    | '=' ExpressionList
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ExpressionListGroup", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_operand(p):
	'''
	Operand     : Literal
	            | OperandName
	            | MethodExpr
	            | left_paren Expression right_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
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
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_operand_name(p):
	'''
	OperandName : identifier
	            | QualifiedIdent
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "OperandName", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_literal(p):
	'''
	Literal     : BasicLit
	            | CompositeLit
	            | FunctionLit
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Literal", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_basic_lit(p):
	'''
	BasicLit    : int_lit
	            | float_lit
	            | rune_lit
	            | string_literal
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "BasicLit", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_composite_lit(p):
	'''
	CompositeLit : LiteralType LiteralValue
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "CompositeLit", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_literal_type(p):
	'''
	LiteralType : StructType
	            | ArrayType
	            | left_sq_paren spread_op right_sq_paren ElementType
	            | SliceType
	            | MapType
	            | TypeName
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "LiteralType", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_literal_value(p):
	'''
	LiteralValue : left_block_bracket right_block_bracket
	             | left_block_bracket ElementList right_block_bracket
	             | left_block_bracket ElementList comma right_block_bracket
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "LiteralValue", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_element_list(p):
	'''
	ElementList : KeyedElement
	            | ElementList comma KeyedElement
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ElementList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_keyed_element(p):
	'''
	KeyedElement : Element
	             | Key label_op Element
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "KeyedElement", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_key(p):
	'''
	Key          : FieldName
	             | Expression
	             | LiteralValue
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Key", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_field_name(p):
	'''
	FieldName    : identifier
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "FieldName", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_element(p):
	'''
	Element      : Expression
	             | LiteralValue
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Element", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_function_lit(p):
	'''
	FunctionLit  : keyword_func Function
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "FunctionLit", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_function(p):
	'''
	Function     : Signature FunctionBody
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Function", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_function_body(p):
	'''
	FunctionBody : Block
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "FunctionBody", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_block(p):
	'''
	Block        : left_block_bracket StatementList right_block_bracket
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Block", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_statement_list(p):
	'''
	StatementList : empty
	              | StatementList Statement stmt_end
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "StatementList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_statement(p):
	'''
	Statement    : Declaration
	             | LabeledStmt
	             | SimpleStmt
	             | ReturnStmt
	             | BreakStmt
	             | ContinueStmt
	             | GotoStmt
	             | FallthroughStmt
	             | Block
	             | IfStmt
	             | SwitchStmt
	             | ForStmt
	             | DeferStmt
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
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
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_labeled_stmt(p):
	'''
	LabeledStmt : Label label_op Statement
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "LabeledStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_label(p):
	'''
	Label       : identifier
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Label", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_simple_stmt(p):
	'''
	SimpleStmt : EmptyStmt
	           | ExpressionStmt
	           | IncDecStmt
	           | Assignment
	           | ShortVarDecl
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "SimpleStmt", "id": str(counter)}
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
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_empty_stmt(p):
	'''
	EmptyStmt : empty
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "EmptyStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_expression_stmt(p):
	'''
	ExpressionStmt : Expression
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ExpressionStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_inc_dec_stmt(p):
	'''
	IncDecStmt : Expression inc_dec_op
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "IncDecStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_assignment(p):
	'''
	Assignment : ExpressionList assign_op ExpressionList
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Assignment", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_short_var_decl(p):
	'''
	ShortVarDecl : IdentifierList ':=' ExpressionList
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ShortVarDecl", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_return_stmt(p):
	'''
	ReturnStmt : keyword_return
	           | keyword_return ExpressionList
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ReturnStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_break_stmt(p):
	'''
	BreakStmt  : keyword_break
	           | keyword_break Label
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "BreakStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_continue_stmt(p):
	'''
	ContinueStmt : keyword_continue
	             | keyword_continue Label
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ContinueStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_goto_stmt(p):
	'''
	GotoStmt : keyword_goto Label
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "GotoStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_fallthrough_stmt(p):
	'''
	FallthroughStmt : keyword_fallthrough
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "FallthroughStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_if_stmt(p):
	'''
	IfStmt : keyword_if Expression Block
	       | keyword_if SimpleStmt stmt_end Expression Block
	       | keyword_if Expression Block keyword_else IfStmtGrp
	       | keyword_if SimpleStmt stmt_end Expression Block keyword_else IfStmtGrp
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "IfStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	elif (len(p) == 8):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5], p[6], p[7]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_if_stmt_grp(p):
	'''
	IfStmtGrp : IfStmt
	          | Block
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "IfStmtGrp", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_switch_stmt(p):
	'''
	SwitchStmt : ExprSwitchStmt
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "SwitchStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_expr_switch_stmt(p):
	'''
	ExprSwitchStmt : keyword_switch left_block_bracket ExprCaseClauseList right_block_bracket
	               | keyword_switch SimpleStmt stmt_end left_block_bracket ExprCaseClauseList right_block_bracket
	               | keyword_switch Expression left_block_bracket ExprCaseClauseList right_block_bracket
	               | keyword_switch SimpleStmt stmt_end Expression left_block_bracket ExprCaseClauseList right_block_bracket
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ExprSwitchStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 7):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5], p[6]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	elif (len(p) == 8):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5], p[6], p[7]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_expr_case_clause_list(p):
	'''
	ExprCaseClauseList : empty
	                   | ExprCaseClauseList ExprCaseClause
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ExprCaseClauseList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_expr_case_clause(p):
	'''
	ExprCaseClause : ExprSwitchCase label_op StatementList
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ExprCaseClause", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_expr_switch_case(p):
	'''
	ExprSwitchCase : keyword_case ExpressionList
	               | keyword_default
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ExprSwitchCase", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_for_stmt(p):
	'''
	ForStmt : keyword_for Block
	        | keyword_for ConditionGrp Block
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ForStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_condition_grp(p):
	'''
	ConditionGrp : Condition
	             | ForClause
	             | RangeClause
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ConditionGrp", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_condition(p):
	'''
	Condition : Expression
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Condition", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_for_clause(p):
	'''
	ForClause : stmt_end stmt_end
	          | InitStmt stmt_end stmt_end
	          | stmt_end Condition stmt_end
	          | stmt_end stmt_end PostStmt
	          | InitStmt stmt_end Condition stmt_end
	          | stmt_end Condition stmt_end PostStmt
	          | InitStmt stmt_end stmt_end PostStmt
	          | InitStmt stmt_end Condition stmt_end PostStmt
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ForClause", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_init_stmt(p):
	'''
	InitStmt : SimpleStmt
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "InitStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_post_stmt(p):
	'''
	PostStmt : SimpleStmt
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "PostStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_range_clause(p):
	'''
	RangeClause : keyword_range Expression
	            | ExpressionList '=' keyword_range Expression
	            | IdentifierList ':=' keyword_range Expression
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "RangeClause", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_defer_stmt(p):
	'''
	DeferStmt : keyword_defer Expression
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "DeferStmt", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_expression_list(p):
	'''
	ExpressionList : Expression
	               | ExpressionList comma Expression
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ExpressionList", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_expression(p):
	'''
	Expression : UnaryExpr
	           | Expression binary_op Expression
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Expression", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_unary_expr(p):
	'''
	UnaryExpr : PrimaryExpr
	          | unary_op UnaryExpr
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "UnaryExpr", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_primary_expr(p):
	'''
	PrimaryExpr : Operand
	            | Conversion
	            | ForCompExpr
	            | PrimaryExpr Selector
	            | PrimaryExpr Index
	            | PrimaryExpr Slice
	            | PrimaryExpr TypeAssertion
	            | PrimaryExpr Arguments
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "PrimaryExpr", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_conversion(p):
	'''
	Conversion : Type left_paren Expression right_paren
	           | Type left_paren Expression comma right_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Conversion", "id": str(counter)}
	counter += 1
	if (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_method_expr(p):
	'''
	MethodExpr : ReceiverType dot MethodName
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "MethodExpr", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_receiver_type(p):
	'''
	ReceiverType : TypeName
	             | left_paren '*' TypeName right_paren
	             | left_paren ReceiverType right_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ReceiverType", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_for_comp_expr(p):
	'''
	ForCompExpr : left_sq_paren Expression '|' RangeClause right_sq_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "ForCompExpr", "id": str(counter)}
	counter += 1
	if (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_selector(p):
	'''
	Selector : dot identifier
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Selector", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_index(p):
	'''
	Index : left_sq_paren Expression right_sq_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Index", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_slice(p):
	'''
	Slice : left_sq_paren label_op right_sq_paren
	      | left_sq_paren Expression label_op right_sq_paren
	      | left_sq_paren label_op Expression right_sq_paren
	      | left_sq_paren Expression label_op Expression right_sq_paren
	      | left_sq_paren label_op Expression label_op Expression right_sq_paren
	      | left_sq_paren Expression label_op Expression label_op Expression right_sq_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Slice", "id": str(counter)}
	counter += 1
	if (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	elif (len(p) == 7):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5], p[6]]
	elif (len(p) == 8):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5], p[6], p[7]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_type_assertion(p):
	'''
	TypeAssertion : dot left_paren Type right_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "TypeAssertion", "id": str(counter)}
	counter += 1
	if (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_arguments(p):
	'''
	Arguments : left_paren right_paren
	          | left_paren ArgIerGroup right_paren
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	'''
	global counter
	p[0] = {"label": "Arguments", "id": str(counter)}
	counter += 1
	if (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	else:
		p[0]['children'] = [p[0]]

def p_arg_ier_group(p):
	'''
	ArgIerGroup : ExpressionList
	              | ExpressionList spread_op
	              | ExpressionList comma
	              | ExpressionList spread_op comma
	              | Type
	              | Type spread_op
	              | Type comma
	              | Type spread_op comma
	              | Type comma ExpressionList
	              | Type comma ExpressionList spread_op
	              | Type comma ExpressionList comma
	              | Type comma ExpressionList spread_op comma
	<<
	p[0]['children'] = [p[1], p[2], p[3], p[4]]
	>>
	
	'''
	global counter
	p[0] = {"label": "ArgIerGroup", "id": str(counter)}
	counter += 1
	if (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 2):
		p[0]['children'] = [p[1]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 3):
		p[0]['children'] = [p[1], p[2]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 4):
		p[0]['children'] = [p[1], p[2], p[3]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 5):
		p[0]['children'] = [p[1], p[2], p[3], p[4]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	elif (len(p) == 6):
		p[0]['children'] = [p[1], p[2], p[3], p[4], p[5]]
	elif (len(p) == 1):
		p[0]['children'] = [p[0]]
	else:
		p[0]['children'] = [p[-1]]


def p_error(p):
	print(p)
	print("Syntax error in input!")

parser = yacc.yacc()

