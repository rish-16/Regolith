from rply import ParserGenerator
from ast_assets import Number, Sub, Sum, Print

class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN', 'SEMI_COLON', 'SUM', 'SUB']
        )
        
    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(p[2])
            
        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def expression(p):
            left = p[0]
            right = p [1]
            
            operator = p[2]
            
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
                
        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)
            
        @self.pg.error
        def error_handle(token):
            return ValueError(token)
            
    def get_parser(self):
        return self.pg.build()