from rply import LexerGenerator

class RegoLexer:
    def __init__(self):
        self.lexer = LexerGenerator()
        
    def create_tokens(self):
        self.lexer.add('PRINT', r'OUTPUT')
        self.lexer.add('NUMBER', '-?\d+')
        self.lexer.add('STRING', '(".+")|(\'.+\')|(\'\')|("")')
        self.lexer.add('NEWLINE', '\n')
        self.lexer.add('IDENTIFIER', '[a-zA-Z_][a-zA-Z0-9_]')
        
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
        
        # variables
        self.lexer.add('VAR_INIT', '(DECLARE)')
        self.lexer.add('=', '=')
        
        # data types
        # self.lexer.add('INTEGER_TYPE', r'INTEGER')
        # self.lexer.add('STRING_TYPE', r'STRING')
        
        self.lexer.ignore('[ \t\r\f\v]+')
        
    def get_lexer(self):
        self.create_tokens()
        
        return self.lexer.build()