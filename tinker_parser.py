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


    # TODO: not recognising if statements
    @_('identifier ASSIGN expression ";"',
       'IF condition THEN commands ELSE commands ENDIF',
       'IF condition THEN commands ENDIF',
       'WHILE condition DO commands ENDWHILE',
       'REPEAT commands UNTIL condition ";"',
    #    'proc_call;',
    # DEBUG:
        # 'IF condition THEN ENDIF ";"',
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
    
    
    # arithmetic expression
    @_('value',
       'value "+" value',
       'value "-" value',
       'value "*" value',
       'value "/" value',
       'value "%" value')
    def expression(self, p):
        return 'expression'
    
    
    # logic statements
    # temporarly unreachable...
    @_('value EQUAL value', # type: ignore
       'value NEQUAL value',
       'value MORE value',
       'value LESS value',
       'value MOREEQ value',
       'value LESSEQ value',)
    def condition(self, p):
        # return (p[1], p[0], p[2])
        return 'condition'
    
    
    # value of a variable
    @_('NUM',
       'identifier')
    def value(self, p):
        # return p[0]
        return 'value'
    
    
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
    