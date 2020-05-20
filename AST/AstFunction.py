class AstFunction:
    def __init__(self, function_name):
        self.name = function_name
        self.expressions = []
        self.function_params = []
        self.return_var = []

    def print_info(self):
        print("Name:")
        print(self.name)
        print("Expressions:")
        print(self.expressions)
        print("Params:")
        print(self.function_params)
        print("Return statement:")
        print(self.return_var)
