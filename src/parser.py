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
            return Print(p)
            
        