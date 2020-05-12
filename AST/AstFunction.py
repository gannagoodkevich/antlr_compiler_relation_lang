class AstFunction:
    def __init__(self, function_name):
        self.name = function_name
        self.expressions = []
        self.function_params = []

    def print_info(self):
        print("Name:")
        print(self.name)
        print("Expressions:")
        print(self.expressions)
        print("Params:")
        print(self.function_params)
