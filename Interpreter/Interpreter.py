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
                    #else:
                        #if value == 'Integer':
                        #    result += "to_i()"
                        #else:
                        #    if value == 'Float':
                        #        result += "to_f()"
                result = result.replace("(", '')
                result = result.replace(")", '')
                self.file_.write(result)
                self.file_.write("\n")
            if expr.__class__.__name__ == 'AstArray':
                result = str(expr.name) + ' = []\n'
                for elem in expr.elements:
                    index = expr.elements.index(elem)
                    result += str(expr.name) + "[" + expr.indexes[index] + "]" + ' = ' + elem + '\n'
                self.file_.write(result)
                self.file_.write("\n")
            if expr.__class__.__name__ == 'AstStringAssignment':
                result = str(expr.var) + ' = '
                for value in expr.value:
                    if not (value == ")" or value == "("):
                        if value == 'String':
                            result += "str("
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
                result = str(expr.var) + ' = ' + "Row("
                result += str(expr.table[0].name) + '('
                for param in expr.table[0].function_params:
                    if param == expr.table[0].function_params[-1]:
                        result += str(param)
                    else:
                        result += str(param) + ', '
                result += "), " + expr.row_vars + ")"
                #if expr.table[0].__class__.__name__ == 'Function_call_assignmentContext':
                #    result += str(expr.table[0].name) + "(" + expr.table[0].params[0] + ", " + expr.table[0].params[0] + ")"+ ", \"" + str(expr.table[0].row_vars) + "\")"
                self.file_.write(result)
                self.file_.write("\n")
            if expr.__class__.__name__ == 'AstFunctionCall':
                result = str(expr.name) + '('
                for param in expr.function_params:
                    if param == expr.function_params[-1]:
                        result += str(param)
                    else:
                        result += str(param) + ', '
                result += ")"
                self.file_.write(result)
                self.file_.write("\n")
            if expr.__class__.__name__ == 'AstForStatement':
                result = 'for '+ expr.var + ' in range(' + expr.start_value[1] + ', ' + expr.end_value[2] + '):'
                self.file_.write(result)
                self.file_.write("\n")
                for e in expr.expressions:
                    if e.__class__.__name__ == 'AstFunctionCall':
                        result = '\t' + str(e.name) + '('
                        for param in e.function_params:
                            if param == e.function_params[-1]:
                                result += str(param)
                            else:
                                result += str(param) + ', '
                        result += ")"
                        self.file_.write(result)
                        self.file_.write("\n")
                    if e.__class__.__name__ == 'AstArray':
                        result = '\t' + str(e.name) + ' = []\n'
                        for elem in e.elements:
                            index = e.elements.index(elem)
                            result += '\t' + str(e.name) + "[" + e.indexes[index] + "]" + ' = ' + elem + '\n'
                        self.file_.write(result)
                        self.file_.write("\n")
                    if e.__class__.__name__ == 'AstStringAssignment':
                        result = '\t' + str(e.var) + ' = '
                        for value in e.value:
                            if value == 'String':
                                result += "str("
                            else:
                                if not (value == ")" or value == "("):
                                    result += str(value)
                        result = result.replace(")", '')
                        if "str(" in result:
                            result += ")"
                        self.file_.write(result)
                        self.file_.write("\n")
                    if e.__class__.__name__ == 'AstVariable':
                        result = '\t' + str(e.name) + ' ' + e.operator + ' '
                        for value in e.value:
                            if value == 'String':
                                result += "str("
                            else:
                                if not (value == ")" or value == "("):
                                    result += str(value)
                        if "str(" in result:
                            result += ')'
                        self.file_.write(result)
                        self.file_.write("\n")
                    if e.__class__.__name__ == 'AstIntAssignment' or e.__class__.__name__ == 'AstFloatAssignment':
                        result = '\t' + str(e.var) + ' = '
                        for value in e.value:
                            if not (value == "Integer" or value == "Float"):
                                result += value
                            #else:
                                #if value == 'Integer':
                                #    result += "to_i()"
                                #else:
                                #    if value == 'Float':
                                #        result += "to_f()"
                        result = result.replace("(", '')
                        result = result.replace(")", '')
                        self.file_.write(result)
                        self.file_.write("\n")
            if expr.__class__.__name__ == 'AstIfStatement':
                result = 'if '+ expr.var[0] + ' ' + expr.operator + ' ' + expr.condition[0] + ':'
                self.file_.write(result)
                self.file_.write("\n")
                for e in expr.if_expressions:
                    if e.__class__.__name__ == 'AstFunctionCall':
                        result = '\t' + str(e.name) + '('
                        for param in e.function_params:
                            if param == e.function_params[-1]:
                                result += str(param)
                            else:
                                result += str(param) + ', '
                        result += ")"
                        self.file_.write(result)
                        self.file_.write("\n")
                    if e.__class__.__name__ == 'AstArray':
                        result = '\t' + str(e.name) + ' = []\n'
                        for elem in e.elements:
                            index = e.elements.index(elem)
                            result += '\t' + str(e.name) + "[" + e.indexes[index] + "]" + ' = ' + elem + '\n'
                        self.file_.write(result)
                        self.file_.write("\n")
                    if e.__class__.__name__ == 'AstStringAssignment':
                        result = '\t' + str(e.var) + ' = '
                        for value in e.value:
                            if value == 'String':
                                result += "str("
                            else:
                                if not (value == ")" or value == "("):
                                    result += str(value)
                        result = result.replace(")", '')
                        if "str(" in result:
                            result += ")"
                        self.file_.write(result)
                        self.file_.write("\n")
                    if e.__class__.__name__ == 'AstVariable':
                        result = '\t' + str(e.name) + ' ' + e.operator + ' '
                        for value in e.value:
                            if value == 'String':
                                result += "str("
                            else:
                                if not (value == ")" or value == "("):
                                    result += str(value)
                        if "str(" in result:
                            result += ')'
                        self.file_.write(result)
                        self.file_.write("\n")
                    if e.__class__.__name__ == 'AstIntAssignment' or e.__class__.__name__ == 'AstFloatAssignment':
                        result = '\t' + str(e.var) + ' = '
                        for value in e.value:
                            if not (value == "Integer" or value == "Float"):
                                result += value
                            #else:
                                #if value == 'Integer':
                                #    result += "to_i()"
                                #else:
                                #    if value == 'Float':
                                #        result += "to_f()"
                        result = result.replace("(", '')
                        result = result.replace(")", '')
                        self.file_.write(result)
                        self.file_.write("\n")
                if len(expr.else_expressions) != 0:
                    self.file_.write("else:\n")
                    for e in expr.else_expressions:
                        if e.__class__.__name__ == 'AstFunctionCall':
                            result = '\t' + str(e.name) + '('
                            for param in e.function_params:
                                if param == e.function_params[-1]:
                                    result += str(param)
                                else:
                                    result += str(param) + ', '
                            result += ")"
                            self.file_.write(result)
                            self.file_.write("\n")
                        if e.__class__.__name__ == 'AstStringAssignment':
                            result = '\t' + str(e.var) + ' = '
                            for value in e.value:
                                if value == 'String':
                                    result += "str("
                                else:
                                    if not (value == ")" or value == "("):
                                        result += str(value)
                            result = result.replace(")", '')
                            if "str(" in result:
                                result += ")"
                            self.file_.write(result)
                            self.file_.write("\n")
                        if e.__class__.__name__ == 'AstVariable':
                            result = '\t' + str(e.name) + ' ' + e.operator + ' '
                            for value in e.value:
                                if value == 'String':
                                    result += "str("
                                else:
                                    if not (value == ")" or value == "("):
                                        result += str(value)
                            if "str(" in result:
                                result += ')'
                            self.file_.write(result)
                            self.file_.write("\n")
                        if e.__class__.__name__ == 'AstIntAssignment' or e.__class__.__name__ == 'AstFloatAssignment':
                            result = '\t' + str(e.var) + ' = '
                            for value in e.value:
                                if not (value == "Integer" or value == "Float"):
                                    result += value
                                #else:
                                    #if value == 'Integer':
                                    #    result += "to_i()"
                                    #else:
                                    #    if value == 'Float':
                                    #        result += "to_f()"
                            result = result.replace("(", '')
                            result = result.replace(")", '')
                            self.file_.write(result)
                            self.file_.write("\n")
        for function in self.ast.functions:
            result = 'def ' + str(function.name) + '('
            for param in function.function_params:
                if param == function.function_params[-1]:
                    result += str(param)
                else:
                    result += str(param) + ', '
            result += "):"
            self.file_.write(result)
            self.file_.write("\n")
            for expr in function.expressions:
                if expr.__class__.__name__ == 'AstIntAssignment' or expr.__class__.__name__ == 'AstFloatAssignment':
                    result = '\t' + str(expr.var) + ' = '
                    for value in expr.value:
                        if not (value == "Integer" or value == "Float"):
                            result += value
                        #else:
                            #if value == 'Integer':
                            #    result += "to_i()"
                            #else:
                            #    if value == 'Float':
                            #        result += "to_f()"
                    result = result.replace("(", '')
                    result = result.replace(")", '')
                    self.file_.write(result)
                    self.file_.write("\n")
                if expr.__class__.__name__ == 'AstArray':
                    result = '\t' + str(expr.name) + ' = []\n'
                    for elem in expr.elements:
                        index = expr.elements.index(elem)
                        result += '\t' + str(expr.name) + "[" + expr.indexes[index] + "]" + ' = ' + elem + '\n'
                    self.file_.write(result)
                    self.file_.write("\n")
                if expr.__class__.__name__ == 'AstStringAssignment':
                    result = '\t' + str(expr.var) + ' = '
                    for value in expr.value:
                        if not (value == ")" or value == "("):
                            if value == 'String':
                                result += "str("
                            else:
                                if not value == ")":
                                    result += value
                    result = result.replace(")", '')
                    if "str(" in result:
                        result += ")"
                    self.file_.write(result)
                    self.file_.write("\n")
                if expr.__class__.__name__ == 'AstColumnAssignment':
                    result = '\t' + str(expr.var) + ' = ' + "Column(" + str(expr.column_name) + ", \"" + str(expr.type) + "\")"
                    self.file_.write(result)
                    self.file_.write("\n")
                if expr.__class__.__name__ == 'AstRowAssignment':
                    result = '\t' + str(expr.var) + ' = ' + "Row("
                    result += str(expr.table[0].name) + '('
                    for param in expr.table[0].function_params:
                        if param == expr.table[0].function_params[-1]:
                            result += str(param)
                        else:
                            result += str(param) + ', '
                    result += "), " + expr.row_vars + ")"
                    #if expr.table[0].__class__.__name__ == 'Function_call_assignmentContext':
                    #    result += str(expr.table[0].name) + "(" + expr.table[0].params[0] + ", " + expr.table[0].params[0] + ")"+ ", \"" + str(expr.table[0].row_vars) + "\")"
                    self.file_.write(result)
                    self.file_.write("\n")
                if expr.__class__.__name__ == 'AstFunctionCall':
                    result = '\t' + str(expr.name) + '('
                    for param in expr.function_params:
                        if param == expr.function_params[-1]:
                            result += str(param)
                        else:
                            result += str(param) + ', '
                    result += ")"
                    self.file_.write(result)
                    self.file_.write("\n")
            result = '\treturn ' + str(function.return_var[0])
            self.file_.write(result)
            self.file_.write("\n")
        #starting function writing
            print(expr)
