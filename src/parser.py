import ply.yacc as yacc

from tokrules import tokens

counter = 0

def p_empty(p):
        'empty :'
        pass

def p_start(p):
        'SourceFile  : RepeatTopLevelDecl'
        pass

def p_re_top_level(p):
        '''
        RepeatTopLevelDecl : TopLevelDecl RepeatTopLevelDecl
                           | empty
        '''

def p_top_l(p):
        '''
        TopLevelDecl : IMPORT ImportSpec
        '''

def p_import_spec(p):
        '''
        ImportSpec  :  ImportSpecInit ImportPath
        '''
        pass

def p_import_spec_init(p):
        'ImportSpecInit : empty'
        '               | DOT'
        '               | IDENTIFIER'
        pass

def p_import_path(p):
        '''
        ImportPath : STRINGLIT
        '''
        pass

def p_error(p):
        print(p)
        print("Syntax error in input!")

go_parser = yacc.yacc(start="SourceFile")

