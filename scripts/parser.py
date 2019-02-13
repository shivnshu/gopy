import ply.yacc as yacc

from tokrules import tokens

counter = 0

def p_start(p):
  'Start : PackageClause ImportDeclList TopLevelDeclList'
  global counter
  p[0] = {"label": "Start", "id": str(counter), "children": [p[1]]}
  counter += 1

def p_package_clause(p):
  '''
  PackageClause : package PackageName
  '''
  global counter
  p[0] = {"label": "PackageClause", "id": str(counter), "children": [p[1], p[2]]}
  counter += 1

def p_package_name(p):
  '''
  PackageName : IDENTIFIER
  '''
  global counter
  p[0] = {"label": p[1], "id": str(counter), "children": []}
  counter += 1

def p_package(p):
  '''
  package : PACKAGE
  '''
  global counter
  p[0] = {"label": p[1], "id": str(counter), "children": []}
  counter += 1

def p_import_path(p):
  '''
  ImportPath : STRINGLIT
  '''
  global counter
  p[0] = {"label": p[1], "id": str(counter), 'children': []}
  counter += 1

def p_import_spec(p):
  '''
  ImportSpec : ImportPath
             | dot ImportPath
             | PackageName ImportPath
  '''
  global counter
  p[0] = {'label': 'ImportSpec', 'id': str(counter)}
  if (len(p) == 2):
    p[0]['children'] = [p[1]]
  else:
    p[0]['children'] = [p[1], p[2]]
  counter += 1

def p_import_list(p):
  '''
  ImportList : empty
             | ImportList ImportSpec
  '''
  global counter
  p[0] = {'label': 'ImportList', 'id': str(counter)}
  if (len(p) == 1):
    p[0]['children'] = []
  else:
    p[0]['children'] = [p[1], p[2]]
  counter += 1

def p_import_decl(p):
  '''
  ImportDecl : keyword_import ImportSpec
             | keyword_import left_paren ImportList right_paren
  '''
  global counter
  p[0] = {'label': 'ImportDecl', 'id': str(counter)}
  if (len(p) == 3):
    p[0]['children'] = [p[1], p[2]]
  else:
    p[0]['children'] = [p[1], p[2], p[3], p[4]]
  counter += 1

if p_import_decl_list(p):
  '''
  ImportDeclList : empty
                 | ImportDeclList ImportDecl
  '''
  global counter
  p[0] = {'label': 'ImportDeclList', 'id': str(counter)}
  if (len(p) == 1):
    p[0]['children'] = []
  else:
    p[0]['children'] = [p[1], p[2]]
  counter += 1

def p_top_level_decl_list(p):
  '''
  TopLevelDeclList : empty
                   | TopLevelDeclList TopLevelDecl
  '''
  global counter
  p[0] = {'label': 'TopLevelDeclList', 'id': str(counter)}
  if (len(p) == 1):
    p[0]['children'] = []
  else:
    p[0]['children'] = [p[1], p[2]]
  counter += 1

def p_top_level_decl(p):
  '''
  TopLevelDecl : Declaration
               | FunctionDecl
               | MethodDecl
  '''
  global counter
  p[0] = {'label': 'TopLevelDecl', 'id': str(counter), 'children': [p[1]]}
  counter += 1

def p_function_decl(p):
  '''
  FunctionDecl : keyword_func FunctionName Function
               | keyword_func FunctionName Signature
  '''
  global counter
  p[0] = {'label': 'FunctionDecl', 'id': str(counter), 'children': [p[1], p[2]. p[3]]}
  counter += 1

def p_function_name(p):
  '''
  FunctionName : IDENTIFIER
  '''
  global counter
  p[0] = {'label': p[1], 'id': str(counter), 'children': []}
  counter += 1

def p_method_decl(p):
  '''
  MethodDecl : keyword_func Receiver MethodName Function
             | keyword_func Receiver MethodName Signature
  '''
  global counter
  p[0] = {'label': 'MethodDecl', 'id': str(counter), 'children': [p[1], p[2], p[3], p[4]]}
  counter += 1

def p_receiver(p):
  '''
  Receiver : Parameters
  '''
  global counter
  p[0] = {'label': 'Receiver', 'id': str(counter), 'children': [p[1]]}
  counter += 1

def p_declaration(p):
  '''
  Declaration : ConstDecl
              | TypeDecl
              | VarDecl
  '''
  global counter
  p[0] = {'label': 'Declaration', 'id': str(counter), 'children': [p[1]]}
  counter += 1

def p_const_decl(p):
  '''
  ConstDecl : keyword_const ConstGroup
  '''
  global counter
  p[0] = {'label': 'ConstDecl', 'id': str(counter), 'children': [p[1], p[2]]}
  counter += 1

def p_const_group(p):
  '''
  ConstGroup : ConstSpec
             | left_paren ConstSpecList right_paren
  '''
  global counter
  p[0] = {'label': 'ConstGroup', 'id': str(counter)}
  if (len(p) == 2):
    p[0]['children'] = [p[1]]


def p_error(p):
  print(p)
  print("Syntax error in input!")

parser = yacc.yacc()

s = '''
package main
'''
result = parser.parse(s)
print(result)
