from rply import LexerGenerator

class RegoLexer:
    def __init__(self):
        self.lexer = LexerGenerator()
        
    def create_tokens(self):
        self.lexer.add('PRINT', r'OUTPUT')
        self.lexer.add('NUMBER', '\d+')
        
        # operations
        self.lexer.add('ADD', r'\+')
        self.lexer.add('SUB', r'\-')
        
        # self.lexer.add('SEMI_COLON', r'\;')
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
    
        self.lexer.ignore('\s+')
        
    def get_lexer(self):
        self.create_tokens()
        
        return self.lexer.build()