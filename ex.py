import sys
from antlr4 import *
from like_rubyLexer import like_rubyLexer
from like_rubyParser import like_rubyParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = like_rubyLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = like_rubyParser(stream)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)
