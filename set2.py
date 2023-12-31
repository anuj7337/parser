import ply.lex as lex
import ply.yacc as yacc

# Define a list of Scala keywords
scala_keywords = {
    'object': 'OBJECT',
    'val': 'VAL',
    'var': 'VAR',
    'List': 'LIST',
    'Array': 'ARRAY',
    'Queue': 'QUEUE',
    'Map': 'MAP',
    'Set': 'SET',
    'Boolean': 'BOOLEAN',
    'Byte': 'BYTE',
    'Short': 'SHORT',
    'Char': 'CHAR',
    'Int': 'INT',
    'Long': 'LONG',
    'Float': 'FLOAT',
    'Double': 'DOUBLE',
    'String': 'STRING'
}

# Token names
tokens = ['NUM', 'ID', 'COLON', 'EQUALTO', 'LBRACES', 'RBRACES', 'SQBRACL', 'SQBRACR', 'COMMA', 'BRACL', 'BRACR', 'QUOTES', 'ARROW'] + list(scala_keywords.values())

# Regular expressions for simple tokens
t_COMMA = r'\,'
t_EQUALTO = r'\='
t_COLON = r'\:'
t_SQBRACL = r'\['
t_SQBRACR = r'\]'
t_LBRACES = r'\{'
t_RBRACES = r'\}'
t_BRACL = r'\('
t_BRACR = r'\)'
t_QUOTES = r'\"'
t_ARROW = r'\->'

def t_NUM(t):
    r'\d+'
    t.type = scala_keywords.get(t.value, 'NUM')
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9$#]*'
    t.type = scala_keywords.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_start(p):
    'start : setd'
    print("VALID")

def p_setd(p):
    '''setd : VAL ID COLON SET SQBRACL type SQBRACR EQUALTO SET BRACL content BRACR 
            | VAL ID EQUALTO SET BRACL content BRACR
            | VAR ID COLON SET SQBRACL type SQBRACR EQUALTO SET BRACL content BRACR
            | VAR ID EQUALTO SET BRACL content BRACR
    '''

def p_type(p):
    '''type : STRING
            | INT
            | LONG
            | FLOAT
            | DOUBLE
            | SHORT
            | CHAR
            | BOOLEAN
            | BYTE
    '''

def p_content(p):
    '''content : QUOTES ID QUOTES 
               | QUOTES ID QUOTES COMMA content
               | QUOTES NUM QUOTES 
               | QUOTES NUM QUOTES COMMA content
               | NUM 
               | NUM COMMA content
               |
    '''

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

while True:
    try:
        s = input("Enter: ")
    except EOFError:
        break
    if not s:
        continue
    parser.parse(s)
