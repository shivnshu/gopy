import ply.yacc as yacc

from tokrules import tokens

counter = 0

def p_start(p):
  'Start : PackageClause'
  global counter
  p[0] = {"label": "Start", "id": str(counter), "children": [p[1]]}
  counter += 1

def p_package_clause(p):
  '''
  PackageClause : package PackageLabel
  '''
  global counter
  p[0] = {"label": "PackageClause", "id": str(counter), "children": [p[1], p[2]]}
  counter += 1

def p_package_label(p):
  '''
  PackageLabel : IDENTIFIER
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

def p_error(p):
  print(p)
  print("Syntax error in input!")

parser = yacc.yacc()

s = '''
package main
'''
result = parser.parse(s)
print(result)
