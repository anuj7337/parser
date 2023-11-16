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
    'start : queued'
    print("VALID")

def p_queued(p):
    'queued : VAR ID EQUALTO QUEUE BRACL qucon BRACR'

def p_qucon(p):
    '''qucon : NUM
             | NUM COMMA qucon
             | QUOTES ID QUOTES
             | QUOTES ID QUOTES COMMA qucon
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