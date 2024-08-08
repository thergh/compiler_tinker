from sly import Parser
from tinker_lexer import TinkerLexer

class TinkerParser(Parser):
    tokens = TinkerLexer.tokens
    
    # put grammar here

    @_('args_decl "," PID',
       'args_decl "," T PID',
       'PID',
       'T PID')
    def args_decl(self, p):
        return 'args_decl'

    @_('args "," PID',
       'PID')
    def args(self, p):
        return 'args'

    # arithmetic expression
    @_('value',
       'value "+" value',
       'value "-" value',
       'value "*" value',
       'value "/" value',
       'value "%" value',)
    def expression(self, p):
        return 'expression'
    
    # logic statements
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
    @_('PID')               # TODO: arrays
    def identifier(self, p):
        # return p.PID
        return 'identifier'
        
    
if __name__ == '__main__':
    lexer = TinkerLexer()
    parser = TinkerParser()

    while True:
        try:
            input_text = input('calc > ')
            result = parser.parse(lexer.tokenize(input_text))
            print(result)
        except EOFError:
            break