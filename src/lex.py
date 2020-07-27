from rply import LexerGenerator

class RegoLexer:
    def __init__(self):
        self.lexer = LexerGenerator()
        
    def _add_tokens(self):
        # print
        self.lexer.add('PRINT', r'OUTPUT')
        
        # parenthesis
        self.lexer.add('OPEN_PARAN', r'\(')
        self.lexer.add('CLOSE_PARAN', r'\)')
        
        # semi color
        self.lexer.add('SEMI_COLON', r'\;')
        
        # operators
        self.lexer.add('ADD', r'\+')
        self.lexer.add('SUB', r'\-')
        
        # number
        self.lexer.add('NUMBER', '\d+')
    
        # ignore spaces
        self.lexer.ignore('\s+')
        
    def get_lexer(self):
        self._add_tokens()
        
        return self.lexer.build()