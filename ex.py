import sys
from antlr4 import *
from like_rubyLexer import like_rubyLexer
from like_rubyParser import like_rubyParser
from visitors.main_visitor import Visitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = like_rubyLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = like_rubyParser(stream)
    tree = parser.prog()
    #print(tree.toStringTree(recog=parser))
    visitor = Visitor()
    visitor.visit(tree)
    # print(visitor.memory)
    visitor.programm.print_info()

if __name__ == '__main__':
    main(sys.argv)
    # visitor = Visitor()
    # visitor.visitProg(parser.prog)
