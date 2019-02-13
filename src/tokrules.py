# Module: tokrules

import ply.lex as lex

keywords = ['break', 'default', 'func', 'interface', 'select', 'case', 'defer',
            'go', 'map', 'struct', 'chan', 'else', 'goto', 'package', 'switch',
            'const', 'fallthrough', 'if', 'range', 'type', 'continue', 'for',
            'import', 'return', 'var']
constants = ['true', 'false', 'nil', 'iota']

punctuations = ['LPAREN', 'LSQUARE', 'LCURLY', 'COMMA', 'DOT', 'RPAREN', 'RSQUARE',
                'RCURLY', 'SEMICOLON', 'COLON']

operators = ['ADD', 'MINUS', 'MULT', 'DIV', 'MOD', 'AND', 'OR', 'POW', 'LSHIFT',
             'RSHIFT', 'AND_POW', 'PLUS_EQ', 'MINUS_EQ', 'MULT_EQ', 'DIV_EQ', 'MOD_EQ',
             'AND_EQ', 'OR_EQ', 'POW_EQ', 'LSHIFT_EQ', 'RSHIFT_EQ', 'AND_POW_EQ',
             'AND_AND', 'OR_OR', 'RECEIVE', 'PLUS_PLUS', 'MINUS_MINUS', 'EQ_EQ', 'LESS',
             'GREATER', 'EQ', 'NOT', 'NOT_EQ', 'LESS_EQ', 'GREATER_EQ', 'SHORT_ASSIGN',
             'DOT_DOT_DOT']

tokens = ['STRINGLIT', 'COMMENT', 'IDENTIFIER', 'RUNELIT', 'FLOATINGLIT',
          'IMAGINARYLIT', 'INTEGERLIT'] \
            + [k.upper() for k in keywords] \
            + [k.upper() for k in constants] \
            + [k for k in punctuations] \
            + [k for k in operators]

t_ignore = ' |\t|\n'

t_STRINGLIT = r'`[^\`]+`|\"(.*|\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8}|\\(a|b|f|n|r|t|v|\\|\'|\")|\\[0-7]{3}|\\x[0-7]{2})\"'
t_COMMENT =  r'\/\/[^\n]*|\/\*((.|\n)*)\*\/'
t_RUNELIT = r'\'([^’\n]|\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8}|\\(a|b|f|n|r|t|v|\\|\'|\")|\\[0-7]{3}|\\x[0-7]{2})\''
t_FLOATINGLIT = r'[0-9]+\.[0-9]*([eE][+-]?[0-9]+)?|[0-9]+[eE][+-]?[0-9]+|\.[0-9]+([eE][+-]?[0-9]+)?'
t_IMAGINARYLIT = r'([0-9]+|[0-9]+\.[0-9]*([eE][+-]?[0-9]+)?|[0-9]+[eE][+-]?[0-9]+|\.[0-9]+([eE][+-]?[0-9]+)?)i'
t_INTEGERLIT = r'0|[1-9][0-9]*|0[0-7]+|0[xX][0-9a-fA-F]+'

t_ADD = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_AND = r'&'
t_OR = r'\|'
t_POW = r'\^'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_AND_POW = r'&\^'
t_PLUS_EQ = r'\+='
t_MINUS_EQ = r'-='
t_MULT_EQ = r'\*='
t_DIV_EQ = r'/='
t_MOD_EQ = r'%='
t_AND_EQ = r'&='
t_OR_EQ = r'\|='
t_POW_EQ = r'\^='
t_LSHIFT_EQ = r'<<='
t_RSHIFT_EQ = r'>>='
t_AND_POW_EQ = r'&\^='
t_AND_AND = r'&&'
t_OR_OR = r'\|\|'
t_RECEIVE = r'<-'
t_PLUS_PLUS = r'\+\+'
t_MINUS_MINUS = r'--'
t_EQ_EQ = r'=='
t_LESS = r'<'
t_GREATER = r'>'
t_EQ = r'='
t_NOT = r'!'
t_NOT_EQ = r'!='
t_LESS_EQ = r'<='
t_GREATER_EQ = r'>='
t_SHORT_ASSIGN = r':='
t_DOT_DOT_DOT = r'\.\.\.'
t_LPAREN = r'\('
t_LSQUARE = r'\['
t_LCURLY = r'\{'
t_COMMA = r','
t_DOT = r'\.'
t_RPAREN = r'\)'
t_RSQUARE = r'\]'
t_RCURLY = r'\}'
t_SEMICOLON = r';'
t_COLON = r':'

def t_IDENTIFIER(t):
    r'[^\W\d][\w]*'
    if t.value in keywords:
        t.type = t.value.upper()
    if t.value in constants:
        t.type = t.value.upper()
    return t

def t_error(t):
     print("Illegal character '%s'" % t.value[0])

lexer = lex.lex()

# data = '''
#  3 + 4 * 10
#    + -20 *2
# (){;:
#  '''

# lexer.input(data)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
