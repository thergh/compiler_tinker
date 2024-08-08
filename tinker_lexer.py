# calclex.py

from sly import Lexer

class TinkerLexer(Lexer):

    # declaring lexer tokens
    tokens = {PID, NUM,
            #   COMMA, SCOLON, HASH, PLUS, MINUS, TIMES,
            #   DIVIDE, MOD,
              EQUAL, NEQUAL, MORE, LESS, MOREEQ, LESSEQ,
              ASSIGN, LPAREN, RPAREN, PROCEDURE, IS, IN, END,
              PROGRAM, IF, THEN, ELSE, ENDIF, WHILE, DO, ENDWHILE,
              REPEAT, UNTIL, READ, WRITE, COMMENT}
    
    literals = {',', ';', '#', '+', '-', '*', '/', '%'}
    
    # the higher a rule, the more priority it gets
    COMMENT = r'#.*\n'
    ignore = ' \t\n'
    
    
    # procedures and commands
    PROCEDURE = r'PROCEDURE'
    IS = r'IS'
    IN = 'IN'
    END = 'END'
    PROGRAM = 'PROGRAM'
    IF = 'IF'
    THEN = 'THEN'
    ELSE = 'ELSE'
    ENDIF = 'ENDIF'
    WHILE = 'WHILE'
    DO = 'DO'
    ENDWHILE = 'ENDWHILE'
    REPEAT = 'REPEAT'
    UNTIL = 'UNTIL'
    READ = 'READ'
    WRITE = 'WRITE'
    
    # names and numbers
    PID = r'[_a-z]+'            # pidentifier
    NUM = r'0|[1-9]+[0-9]*'     # num - natural number
    # COMMA = r','
    # SCOLON = r";"
    # HASH = r'#'
    
    # arithmetic
    # PLUS = r'\+'
    # MINUS = r'-'
    # TIMES = r'\*'
    # DIVIDE = r'/'
    # MOD = r'%'
    
    # conditions
    EQUAL = r'='
    NEQUAL = r'!='
    MOREEQ = r">="
    LESSEQ = r'<='
    MORE = r'>'
    LESS = r'<'
    
    # misc
    ASSIGN = r':='  # maybe will have to move upwards later
    LPAREN = r'\('
    RPAREN = r'\)'



if __name__ == '__main__':
    lexer = TinkerLexer()
    
    # temporarlyhardcoded source file as input_code.txt
    with open('input_test_1.txt', 'r') as file:
        data = file.read()
        
    # printing all tokens with their values
    for token in lexer.tokenize(data):
        print('type=%r, value=%r' % (token.type, token.value))