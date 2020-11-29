from pprint import pprint
from rply import ParserGenerator
from ast_assets import Program, Number, String, Print, Add, Sub, Mul, Div, Mod, Pow

class RegoParser:
    def __init__(self):
        self.pg = ParserGenerator(
            ['NEWLINE', 'NUMBER', 'STRING', 'PRINT', 'SEMI_COLON', 'OPEN_PAREN', 'CLOSE_PAREN', 'ADD', 'SUB', 'MUL', 'DIV', 'MOD', 'POW'],
            precedence=[('left', ['ADD', 'SUB']), ('left', ['MUL', 'DIV']), ('left', ['MOD', 'POW'])]
        )
        
    def parse(self):
        @self.pg.production('program : statement_list')
        def main(state_list):
            return Program(state_list[0])
        
        @self.pg.production('statement_list : statement SEMI_COLON')
        def statement_list_stmt(tokens):
            return [tokens[0]] # only return the statement and not semicolon
            
        @self.pg.production('statement_list : statement_list statement SEMI_COLON')
        def statement_list(tokens):
            initial = tokens[0]
            initial.append(tokens[1])
            return initial
            
        @self.pg.production('statement_list : statement_list NEWLINE')
        def newline(tokens):
            return tokens[0]
    
        @self.pg.production('statement : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def print_statement(tokens):
            return Print(tokens[2])
            
        @self.pg.production('statement : expression')
        def statement_expr(tokens):
            return tokens[0]
            
        @self.pg.production('expression : NUMBER')
        def expression_number(tokens):
            return Number(int(tokens[0].getstr()))
            
        @self.pg.production('expression : STRING')
        def expression_string(tokens):
            return String(str(tokens[0].getstr()))
            
        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expression_paren(tokens):
            return tokens[1]
            
        @self.pg.production('expression : expression ADD expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression MOD expression')
        @self.pg.production('expression : expression POW expression')
        def expression_binop(tokens):
            left = tokens[0]
            operator = tokens[1]
            right = tokens[2]
            
            if operator.gettokentype() == 'ADD':
                return Add(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)
            elif operator.gettokentype() == 'MOD':
                return Mod(left, right)      
            elif operator.gettokentype() == 'POW':
                return Pow(left, right)
            else:
                raise AssertionError('Operation not possible.')
            
        @self.pg.error
        def error_handler(tokens):
            raise ValueError("Ran into a {} where it wasn't expected.".format(tokens.gettokentype()))
            
    def get_parser(self):
        self.parse()
        return self.pg.build()