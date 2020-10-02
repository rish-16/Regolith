from lex import RegoLexer
from parser import RegoParser

text_input = """
OUTPUT (5 + 234);
OUTPUT (2 + 2);
OUTPUT ("Hello world");
"""

lexer = RegoLexer().get_lexer()
parser = RegoParser().get_parser()

tokens = lexer.lex(text_input)
    
parser.parse(tokens).eval()