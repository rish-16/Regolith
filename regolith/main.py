import argparse
from lex import RegoLexer
from parser import RegoParser

parser = argparse.ArgumentParser(description="Converting Regolith to a command line run language")
parser.add_argument("--file", "-f", type=str, help="File written in Regolith")

args = parser.parse_args()
filename = args.file

lexer = RegoLexer().get_lexer()
parser = RegoParser().get_parser()

with open(filename) as f:
    data = f.read().strip().split("\n")
    data = "".join(data)

tokens = lexer.lex(data)
    
parser.parse(tokens).eval()