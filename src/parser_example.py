import ply.yacc as yacc

from tokrules import tokens
from SymbolTable import SymbolTable
from SymbolTable import SymbolTableLiteralEntry as LiteralEntry
from SymbolTable import SymbolTableVariableEntry as VariableEntry
from SymbolTable import SymbolTableFunctionEntry as FunctionEntry

symTableDict = {"rootSymTable": SymbolTable(None, "rootSymTable")}
symTableSt = ["rootSymTable"]

def p_empty(p):
	'empty :'
	pass

def p_source_file(p):
        '''
        SourceFile  : PackageClause ImportDeclList
        '''
        scope = symTableSt[-1]
        symTable = symTableDict[scope]
        lit = LiteralEntry("lit", 10)
        symTable.put(lit)

def p_package_clause(p):
        '''
        PackageClause  : PACKAGE IDENTIFIER
        '''

def p_import_decl_list(p):
        '''
        ImportDeclList : ImportDecl ImportDeclList
                        | empty
        '''
        print("c")

def p_import_decl(p):
        '''
        ImportDecl    : IMPORT ImportSpecTopList
        '''
        print("d")

def p_import_spec_top_list(p):
        '''
        ImportSpecTopList : ImportSpec
                        | LPAREN ImportSpecList RPAREN
        '''
        print("e")

def p_import_spec_list(p):
        '''
        ImportSpecList : ImportSpec ImportSpecList
                        | empty
        '''
        print("f")

def p_import_spec(p):
        '''
        ImportSpec       :  ImportSpecInit STRINGLIT
        '''
        print("g")

def p_import_spec_init(p):
        '''
        ImportSpecInit : DOT
                        | IDENTIFIER
                        | empty
        '''
        print("h")

def p_error(p):
	print("Error encountered at line number", p.lineno)

go_parser = yacc.yacc(start="SourceFile", write_tables=False)

