import ply.lex as lex

tokens = (
        'ANDAND', #&&
        'COMMA', #,
        'DIVIDE',#/
        'ELSE',#else
        'EQUAL',#=
        'EQUALEQUAL',#==
        'FALSE',#false
        'FUNCTION',#function
        'GE',#>=
        'GT',#>
        'IDENTIFIER',# Like variable names or funtion names
        'IF',#if
        'LBRACE',#{
        'LE',#<=
        'LPAREN',#(
        'LT',#<
        'MINUS',#-
        'NOT',#!
        'NUMBER',#Number
        'OROR',#||
        'PLUS',#+
        'RBRACE',#}
        'RETURN',#return
        'RPAREN',#)
        'SEMICOLON',#;
        'STRING',#"Hello"
        'TIMES',#*
        'TRUE',#true
        'VAR',#var

)

states = (('comment','exclusive'), #/*     */
          )

def t_comment(t):
    r'\/\*'
    t.lexer.begin('comment')

def t_comment_end(t):
    r'\*\/'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.begin('INITIAL')

def t_comment_error(t):
    t.lexer.skip(1)

def t_eolcomment(t):
    r'//.*'
    pass


def t_WHITESPACE(token): #ignore whitespace
    r'[ ]+'
    pass

def t_NUMBER(token):
    r'-?[0-9]+(?:\.[0-9]*)?'
    token.value = float (token.value)
    return token

def t_FUNCTION(t):
    r'function'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_VAR(t):
    r'var'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ANDAND(t):
    r'&&'
    return t


def t_COMMA(t):
    r','
    return t

def t_DIVIDE(t):
    r'/'
    return t

def t_EQUALEQUAL(t):
    r'=='
    return t

def t_EQUAL(t):
    r'='
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_LBRACE(t):
    r'{'
    return t

def t_RBRACE(t):
    r'}'
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_MINUS(t):
    r'-'
    return t

def t_NOT(t):
    r'!'
    return t

def t_OROR(t):
    r'\|\|'
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_TIMES(t):
    r'\*'
    return t

def t_LE(t):
    r'<='
    return t

def t_LT(t):
    r'<'
    return t

def t_GE(t):
    r'>='
    return t

def t_GT(t):
    r'>'
    return t

def t_STRING(token):
    r'"(?:[^"\\]|(?:\\.))*"'
    token.value = token.value[1:-1] #strip off the quotes
    return token


def t_newline(token):
    r'\n'
    token.lexer.lineno += 1

def t_IDENTIFIER(token):## Identifiers are textual string descriptions that refer to program elements,# such as variables and functions
    r'[a-zA-Z][a-zA-Z_]*'
    return token


def t_error(token):
    print "JavaScript lexer : Illegal character " + token.value[0]
    token.lexer.skip(1)

js_lexer = lex.lex()

def test_lexer(input_string):
    js_lexer.input(input_string)
    result = []
    while True:
        tok = js_lexer.token()
        if not tok:break
        result = result + [tok.type,tok.value]
    return result

def test_lexer2(input_string):
    js_lexer.input(input_string)
    result = []
    while True:
        tok = js_lexer.token()
        if not tok:break
        result = result + [tok.type]
    return result

input1 = 'some_identifier -12.34 "a \\"escape\\" b"'
output1 = ['IDENTIFIER', 'some_identifier', 'NUMBER', -12.34, 'STRING', 'a \\"escape\\" b']
print test_lexer(input1) == output1


input2 = '-12x34'
output2 = ['NUMBER', -12.0, 'IDENTIFIER', 'x', 'NUMBER', 34.0]
print test_lexer(input2) == output2

input3 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output3 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print test_lexer2(input3) == output3
input4 = """
if // else mystery
=/*=*/=
true /* false
*/ return"""

output4 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']

print test_lexer2(input4) == output4