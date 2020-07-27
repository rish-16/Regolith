from lex import RegoLexer

text_input = """
OUTPUT (4 + 4 - 2);
"""

lexer = RegoLexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print (token)