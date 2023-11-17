import ply.lex as lex
import ply.yacc as yacc

# Define a dictionary of Scala keywords
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

# List of token names
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
    'start : listd'
    print("VALID")

def p_listd(p):
    '''listd : VAL ID EQUALTO LIST BRACL content BRACR
             | VAL ID COLON LIST SQBRACL type SQBRACR EQUALTO LIST BRACL content BRACR
             | VAL ID EQUALTO LIST BRACL content1 BRACR
             | VAL ID COLON LIST SQBRACL type SQBRACR EQUALTO LIST BRACL content1 BRACR
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
               |
    '''
def p_content1(p):
    '''content1 : NUM
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
