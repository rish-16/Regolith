from rply import LexerGenerator

class RegoLexer:
    def __init__(self):
        self.lexer = LexerGenerator()
        
    def create_tokens(self):
        self.lexer.add('PRINT', r'OUTPUT')
        self.lexer.add('NUMBER', '-?\d+')
        self.lexer.add('STRING', '(".+")|(\'.+\')|(\'\')|("")')
        self.lexer.add('NEWLINE', '\n')
        self.lexer.add('NEWTAB', '\t')
        
        # operations
        self.lexer.add('ADD', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'DIV')
        self.lexer.add('MOD', r'MOD')
        self.lexer.add('POW', r'POW')
        
        self.lexer.add('SEMI_COLON', r'\;')
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        
        # conditionals
        self.lexer.add('IF', r'IF')
        self.lexer.add('THEN', r'THEN')
        self.lexer.add('ELSE IF', r'(ELSE IF)')
        self.lexer.add('ELSE', r'ELSE')
        self.lexer.add('END_IF', r'ENDIF')
        
        # comparatives
        self.lexer.add("GTE", r"(>=)")
        self.lexer.add("LTE", r"(<=)")
        self.lexer.add("EQ", r"(==)")
        self.lexer.add("LT", r"(<)")
        self.lexer.add("GT", r"(>)")
        
        self.lexer.ignore('[ \r\f\v]+')
        
    def get_lexer(self):
        self.create_tokens()
        
        return self.lexer.build()