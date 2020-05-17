class Interpreter:
    def __init__(self, programm_ast,  target_file):
        self.ast = programm_ast
        self.file_ = open(target_file, "w")
        self.file_.flush()
        self.file_.write("#!/usr/bin/python3\n")
        self.file_.write("interpreting begins *\n")

    def interper_programm(self):
        for expr in  self.ast.expressions:
            if expr.__class__.__name__ == 'AstIntAssignment' or expr.__class__.__name__ == 'AstFloatAssignment':
                result = str(expr.var) + ' = '
                for value in expr.value:
                    if not (value == "Integer" or value == "Float"):
                        result += value
                result = result.replace("(", '')
                result = result.replace(")", '')
                self.file_.write(result)
                self.file_.write("\n")
            if expr.__class__.__name__ == 'AstStringAssignment':
                result = str(expr.var) + ' = '
                for value in expr.value:
                    if not (value == ")" or value == "("):
                        if value == 'String':
                            result += "str("
                        else:
                            if value == 'Integer':
                                result += "to_i()"
                            else:
                                if value == 'Float':
                                    result += "to_f()"
                                else:
                                    if not value == ")":
                                        result += value
                result = result.replace(")", '')
                if "str(" in result:
                    result += ")"
                self.file_.write(result)
                self.file_.write("\n")
            if expr.__class__.__name__ == 'AstColumnAssignment':
                result = str(expr.var) + ' = ' + "Column(" + str(expr.column_name) + ", \"" + str(expr.type) + "\")"
                self.file_.write(result)
                self.file_.write("\n")
            if expr.__class__.__name__ == 'AstRowAssignment':
                result = str(expr.var) + ' = ' + "Row(" + str(expr.table) + ", " + expr.row_vars + ")"
                #if expr.table[0].__class__.__name__ == 'Function_call_assignmentContext':
                #    result += str(expr.table[0].name) + "(" + expr.table[0].params[0] + ", " + expr.table[0].params[0] + ")"+ ", \"" + str(expr.table[0].row_vars) + "\")"
                self.file_.write(result)
                self.file_.write("\n")
            print(expr)
