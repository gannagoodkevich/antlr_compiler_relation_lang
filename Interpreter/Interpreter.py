class Interpreter:
    def __init__(self, programm_ast,  target_file):
        self.ast = programm_ast
        self.file_ = open(target_file, "w")
        self.file_.flush()
        self.file_.write("#!/usr/bin/python3\n\n")
        self.file_.write("from RELib.Column import Column\n")
        self.file_.write("from RELib.Row import Row\n")
        self.file_.write("from RELib.Table import Table\n\n")


    def interper_programm(self):

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
                        result += '\t' + str(expr.name) + ".insert(" + expr.indexes[index] + ", " +  elem + ')\n'
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
                if expr.__class__.__name__ == 'AstTableAssignment':
                    result = '\t' + str(expr.var) + ' = ' + "Table("
                    for column in expr.columns:
                        if not column == "Table.new":
                            if not column == "(":
                                if not column == ")":
                                    if column == expr.columns[-1]:
                                        result += str(column)
                                    else:
                                        result += str(column) + ', '
                    result += ")"
                    self.file_.write(result)
                    self.file_.write("\n")
                if expr.__class__.__name__ == 'AstRowAssignment':
                    result = '\t' + str(expr.var) + ' = ' + "Row("
                    result += str(expr.table[0].function_params[0]) + '.' + str(expr.table[0].name) + '('
                    result += "), " + expr.row_vars + ")"
                    #if expr.table[0].__class__.__name__ == 'Function_call_assignmentContext':
                    #    result += str(expr.table[0].name) + "(" + expr.table[0].params[0] + ", " + expr.table[0].params[0] + ")"+ ", \"" + str(expr.table[0].row_vars) + "\")"
                    self.file_.write(result)
                    self.file_.write("\n")
                if expr.__class__.__name__ == 'AstFunctionCall':
                    if expr.name == 'add_row' or expr.name == 'show':
                        result = '\t' + expr.function_params[0] + '.' + str(expr.name) + '('
                        params = expr.function_params
                        params.remove(expr.function_params[0])
                        for param in params:
                            if param == expr.function_params[-1]:
                                result += str(param)
                            else:
                                result += str(param) + ', '
                        result += ")"
                    else:
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
                    result += str(expr.name) + ".insert(" + expr.indexes[index] + ", " +  elem + ')\n'
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
            if expr.__class__.__name__ == 'AstTableAssignment':
                result = str(expr.var) + ' = ' + "Table("
                for column in expr.columns:
                    if not column == "Table.new":
                        if not column == "(":
                            if not column == ")":
                                if column == expr.columns[-1]:
                                    result += str(column)
                                else:
                                    result += str(column) + ', '
                result += ")"
                self.file_.write(result)
                self.file_.write("\n")
            if expr.__class__.__name__ == 'AstRowAssignment':
                result = str(expr.var) + ' = ' + "Row("
                result += str(expr.table[0].function_params[0]) + '.' + str(expr.table[0].name) + '('
                result += "), " + expr.row_vars + ")"
                #if expr.table[0].__class__.__name__ == 'Function_call_assignmentContext':
                #    result += str(expr.table[0].name) + "(" + expr.table[0].params[0] + ", " + expr.table[0].params[0] + ")"+ ", \"" + str(expr.table[0].row_vars) + "\")"
                self.file_.write(result)
                self.file_.write("\n")
            if expr.__class__.__name__ == 'AstFunctionCall':
                if expr.name == 'add_row' or expr.name == 'show':
                    result = expr.function_params[0] + '.' + str(expr.name) + '('
                    params = expr.function_params
                    params.remove(expr.function_params[0])
                    for param in params:
                        if param == expr.function_params[-1]:
                            result += str(param)
                        else:
                            result += str(param) + ', '
                    result += ")"
                else:
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
                        if e.name == 'add_row':
                            result = '\t' + e.function_params[0] + '.' + str(e.name) + '('
                            params = e.function_params
                            params.remove(e.function_params[0])
                            for param in params:
                                if param == e.function_params[-1]:
                                    result += str(param)
                                else:
                                    result += str(param) + ', '
                            result += ")"
                        else:
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
                            result += '\t' + str(e.name) + ".insert(" + e.indexes[index] + ", " +  elem + ')\n'
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
                    if e.__class__.__name__ == 'AstTableAssignment':
                        result = '\t' + str(e.var) + ' = ' + "Table("
                        for column in e.columns:
                            if not column == "Table.new":
                                if not column == "(":
                                    if not column == ")":
                                        if column == e.columns[-1]:
                                            result += str(column)
                                        else:
                                            result += str(column) + ', '
                        result += ")"
                        self.file_.write(result)
                        self.file_.write("\n")
                    if e.__class__.__name__ == 'AstRowAssignment':
                        result = '\t' + str(e.var) + ' = ' + "Row("
                        result += str(e.table[0].function_params[0]) + '.' + str(e.table[0].name) + '('
                        result += "), " + e.row_vars + ")"
                        #if expr.table[0].__class__.__name__ == 'Function_call_assignmentContext':
                        #    result += str(expr.table[0].name) + "(" + expr.table[0].params[0] + ", " + expr.table[0].params[0] + ")"+ ", \"" + str(expr.table[0].row_vars) + "\")"
                        self.file_.write(result)
                        self.file_.write("\n")
            if expr.__class__.__name__ == 'AstIfStatement':
                result = 'if '+ expr.var[0] + ' ' + expr.operator + ' ' + expr.condition[0] + ':'
                self.file_.write(result)
                self.file_.write("\n")
                for e in expr.if_expressions:
                    if e.__class__.__name__ == 'AstFunctionCall':
                        if e.name == 'add_row' or e.name == 'show':
                            result = '\t' + e.function_params[0] + '.' + str(e.name) + '('
                            params = e.function_params
                            params.remove(e.function_params[0])
                            for param in params:
                                if param == e.function_params[-1]:
                                    result += str(param)
                                else:
                                    result += str(param) + ', '
                            result += ")"
                        else:
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
                        result = '\t' + str(expr.name) + ' = []\n'
                        for elem in expr.elements:
                            index = expr.elements.index(elem)
                            result += '\t' + str(expr.name) + ".insert(" + expr.indexes[index] + ", " +  elem + ')\n'
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
                            if e.name == 'add_row':
                                result = '\t' + e.function_params[0] + '.' + str(e.name) + '('
                                params = e.function_params
                                params.remove(e.function_params[0])
                                for param in params:
                                    if param == e.function_params[-1]:
                                        result += str(param)
                                    else:
                                        result += str(param) + ', '
                                result += ")"
                            else:
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
        #starting function writing
