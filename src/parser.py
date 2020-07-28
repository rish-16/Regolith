from rply import ParserGenerator
from ast_assets import Number, Print, Add, Sub, Mul, Div

class RegoParser:
    def __init__(self):
        self.pg = ParserGenerator(
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN', 'ADD', 'SUB', 'MUL', 'DIV'],
            precedence=[('left', ['ADD', 'SUB']), ('left', ['MUL', 'DIV'])]
        )
        
    def parse(self):  
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def program(p):
            return Print(p[2])
            
        @self.pg.production('expression : NUMBER')
        def expression_number(p):
            return Number(int(p[0].getstr()))
            
        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expression_paren(p):
            return p[1]
            
        @self.pg.production('expression : expression ADD expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression_binop(p):
            left = p[0]
            operator = p[1]
            right = p[2]
            
            if operator.gettokentype() == 'ADD':
                return Add(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)
            else:
                raise AssertionError('Operation not possible.')
            
        @self.pg.error
        def error_handler(token):
            raise ValueError("Ran into a {} where it wasn't expected.".format(token.gettokentype()))
            
    def get_parser(self):
        self.parse()
        return self.pg.build()