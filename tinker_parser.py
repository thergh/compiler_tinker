from sly import Parser
from tinker_lexer import TinkerLexer

class TinkerParser(Parser):
    tokens = TinkerLexer.tokens
    
    
    # TODO: procedures
    
    
    @_('PROGRAM IS declarations IN commands END',
       'PROGRAM IS IN commands END')
    def main(self, p):
        return 'main'
    
    
    @_('commands command',
       'command')
    def commands(self, p):
        return 'commands'


    @_('identifier ASSIGN expression ";"',
       'IF condition THEN commands ELSE commands ENDIF',
       'IF condition THEN commands ENDIF',
       'WHILE condition DO commands ENDWHILE',
       'REPEAT commands UNTIL condition ";"',
    #    'proc_call;',
        'READ identifier ";"',
        'WRITE value ";"')
    def command(self, p):
        return 'command'
    
    
    @_('declarations "," PID',
       'declarations "," PID "[" NUM "]"',
       'PID',
       'PID "[" NUM "]"')
    def declarations(self, p):
        return 'declarations'
    
    
    # arithmetic expressions
    
    @_('value')
    def expression(self, p):
        return p[0]
    
    @_('value "+" value')
    def expression(self, p):
        return 'add', p[0], p[2]
    
    @_('value "-" value')
    def expression(self, p):
        return 'sub', p[0], p[2]
    
    @_('value "*" value')
    def expression(self, p):
        return 'mul', p[0], p[2]
    
    @_('value "/" value')
    def expression(self, p):
        return 'div', p[0], p[2]
    
    @_('value "%" value')
    def expression(self, p):
        return 'mod', p[0], p[2]
    
    
    
    # logic statements
    
    @_('value EQUAL value')
    def condition(self, p):
        return 'equal', p[0], p[2]
    
    @_('value NEQUAL value')
    def condition(self, p):
        return 'nequal', p[0], p[2]
    
    @_('value MORE value')
    def condition(self, p):
        return 'more', p[0], p[2]
    
    @_('value LESS value')
    def condition(self, p):
        return 'less', p[0], p[2]
    
    @_('value MOREEQ value')
    def condition(self, p):
        return 'moreeq', p[0], p[2]
    
    @_('value LESSEQ value')
    def condition(self, p):
        return 'lesseq', p[0], p[2]
    
    
    # value of a variable
    @_('NUM',
       'identifier')
    def value(self, p):
        # return p[0]
        return 'value', p[0]
    
    
    # name of a variable
    @_('PID',
       'PID "[" NUM "]"',
       'PID "[" PID "]"')     
    # @_('PID')# TODO: arrays
    def identifier(self, p):
        # return p.PID
        return 'identifier'
        
    
if __name__ == '__main__':
    lexer = TinkerLexer()
    parser = TinkerParser()
    
    # temporarlyhardcoded source file as input_code.txt
    with open('./programs/test_selt.txt', 'r') as file:
        data = file.read()
        
        
    tokens = lexer.tokenize(data)

    # printing all tokens with their values
    # for token in tokens:
    #     print('type=%r, value=%r' % (token.type, token.value))


    
    parsed_result = parser.parse(tokens)
    print(parsed_result)

    # while True:
    #     try:
    #         input_text = input('calc > ')
    #         result = parser.parse(lexer.tokenize(input_text))
    #         print(result)
    #     except EOFError:
    #         break
    