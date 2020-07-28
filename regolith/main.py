from lex import RegoLexer
from parser import RegoParser

text_input = """
OUTPUT (10 MOD 3);
"""

lexer = RegoLexer().get_lexer()
parser = RegoParser().get_parser()

tokens = lexer.lex(text_input)

parser.parse(tokens).eval()