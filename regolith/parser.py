from pprint import pprint
from rply import ParserGenerator
from ast_assets import Program, Number, String, Print, Add, Sub, Mul, Div, Mod, Pow, GTE, LTE, EQ, LT, GT, T1_Conditional, T2_Conditional, T3_Conditional

class RegoParser:
    def __init__(self):
        self.pg = ParserGenerator(
            ['NEWLINE', 'NEWTAB',
            'NUMBER', 
            'STRING', 
            'PRINT', 
            'SEMI_COLON', 
            'OPEN_PAREN', 
            'CLOSE_PAREN', 
            'ADD', 'SUB', 'MUL', 'DIV', 'MOD', 'POW',
            'GTE', 'LTE', 'LT', 'GT', 'EQ',
            'IF', 'THEN', 'ELSE', 'END_IF'],
            precedence=[('left', ['ADD', 'SUB']), ('left', ['MUL', 'DIV']), ('left', ['MOD', 'POW'])]
        )
        
    def parse(self):
        @self.pg.production('program : statement_list')
        def main(state_list):
            print (state_list)
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
            
        @self.pg.production('statement : NEWTAB statement')
        def indented_statement(tokens):
            return tokens[1]
        
        """
        IF 
        ENDIF
        """
        @self.pg.production('statement_list : IF OPEN_PAREN expression CLOSE_PAREN THEN NEWLINE statement_list NEWLINE END_IF')
        def make_conditional_type_1(tokens):
            return [T1_Conditional(tokens[2], tokens[6])]
            
        """
        IF 
        ELSE
        ENDIF
        """
        @self.pg.production('statement_list : IF OPEN_PAREN expression CLOSE_PAREN THEN NEWLINE statement_list NEWLINE ELSE NEWLINE statement_list NEWLINE END_IF')
        def make_conditional_type_2(tokens):
            pprint (tokens)
            return [T2_Conditional(tokens[2], tokens[6], tokens[10])]
            
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
                
        @self.pg.production('expression : expression GT expression')
        @self.pg.production('expression : expression LT expression')
        @self.pg.production('expression : expression GTE expression')
        @self.pg.production('expression : expression LTE expression')
        @self.pg.production('expression : expression EQ expression')
        def compare(tokens):
            left = tokens[0]
            operator = tokens[1]
            right = tokens[2]
            
            if operator.gettokentype() == 'GT':
                return GT(left, right)
            elif operator.gettokentype() == 'LT':
                return LT(left, right)
            elif operator.gettokentype() == 'GTE':
                return GTE(left, right)
            elif operator.gettokentype() == 'LTE':
                return LTE(left, right)
            elif operator.gettokentype() == 'EQ':
                return EQ(left, right)
            else:
                raise AssertionError('Comparison not possible.')
            
        @self.pg.error
        def error_handler(tokens):
            raise ValueError("Ran into a {} where it wasn't expected.".format(tokens.gettokentype()))
            
    def get_parser(self):
        self.parse()
        return self.pg.build()