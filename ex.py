import sys
from antlr4 import *
from like_rubyLexer import like_rubyLexer
from like_rubyParser import like_rubyParser
from visitors.main_visitor import Visitor
from Interpreter.Interpreter import Interpreter

def main(argv):
    input_stream = FileStream(argv[1])
    target_file = sys.argv[2]
    lexer = like_rubyLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = like_rubyParser(stream)
    tree = parser.prog()
    #print(tree.toStringTree(recog=parser))
    visitor = Visitor()
    visitor.visit(tree)
    # print(visitor.memory)
    visitor.programm.print_info()
    print("Functions:")
    for func in visitor.programm.functions:
        func.print_info()
    interper_programm = Interpreter(visitor.programm, target_file)
    interper_programm.interper_programm()

if __name__ == '__main__':
    main(sys.argv)
    # visitor = Visitor()
    # visitor.visitProg(parser.prog)
