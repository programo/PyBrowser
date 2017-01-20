import ply.lex as lex
import re
tokens =(
    'LANGLE', #<
    'LANGLESLASH', #</
    'RANGLE', #>
    'EQUAL', #=
    'STRING', #"hello"
    'WORD', #Any Word
    'WHITESPACE'
      )

states = (
    ('htmlcomment', 'exclusive'),
    )

def t_htmlcomment(token):
    r'<!--'
    token.lexer.begin('htmlcomment') #comment mode begins

def t_htmlcomment_end(token):
    r'-->'
    token.lexer.lineno += token.value.count('\n') #Add the number of occurence of new line in the comment to the line number
    token.lexer.begin('INITIAL') #normal mode begins

def t_htmlcomment_error(token):
    token.lexer.skip(1) #During comment mode, if there is a character other then <!-- or --> then skip over the characters.

def t_WHITESPACE(token):
    r'[ ]+'
    pass

def t_LANGLESLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_STRING(token):
    r'"[^"]*"'
    token.value = token.value[1:-1]
    return token

def t_newline(token):
    r'\n'
    token.lexer.lineno += 1
    pass

def t_WORD(token):
    r'[^\n<> ]+'
    return token



webpage = "<!-- Hello --> ALL"

htmllexer = lex.lex() #Tells out lexical analysis library  that we want to use all of the token definitions above
                      #to make a lexical analyzer and break up strings
htmllexer.input(webpage)#This function call tells which string to break up

#The output of the lexical analyzer is a list of tokens
#Print out the output of the lexical analyzer
while True:
    tok = htmllexer.token() #.token() function returns the next token that is available
    if not tok:break #If there are no more tokens then break from the loop
    print tok

