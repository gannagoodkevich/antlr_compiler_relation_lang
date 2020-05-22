class AstProgramm:
    def __init__(self):
        self.expressions = []
        self.local_variables = []
        self.declared_function_names = ['add_row', 'get_columns']
        self.defined_function_names = []
        self.functions = []
        self.errors = []

    def print_info(self):
        print("Expressions:")
        print(self.expressions)
        print("Local variables:")
        print(self.local_variables)
        print("Declared functions:")
        print(self.declared_function_names)
        print("Defined functions:")
        print(self.defined_function_names)
        print("Funcitons:")
        print(self.functions)
        print("Errors:")
        print(self.errors)

    def add_expression(self, expr):
        #print("Adding expression")
        #self.print_info()
        self.expressions.append(expr)

    def remove_expression(self, expr):
        self.expressions.remove(expr)
