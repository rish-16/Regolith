from lex import RegoLexer
from parser import RegoParser

text_input = """
print (4 + 4 - 2);
"""

lexer = RegoLexer().get_lexer()
tokens = lexer.lex(text_input)

for t in tokens:
    print (t)

pg = RegoParser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()