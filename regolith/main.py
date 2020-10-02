from lex import RegoLexer
from parser import RegoParser

text_input = """
OUTPUT ("Hello, world! This is Regolith :D");
OUTPUT ("Hello, world! This is Regolith :D");
"""

lexer = RegoLexer().get_lexer()
parser = RegoParser().get_parser()

tokens = lexer.lex(text_input)
    
parser.parse(tokens).eval()