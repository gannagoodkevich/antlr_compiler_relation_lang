class AstFunctionCall:
    def __init__(self):
        self.name = ""
        self.function_result = []
        self.function_params = []

    def print_info(self):
        print("Name:")
        print(self.name)
        print("Params:")
        print(self.function_params)
        print("Result:")
        print(self.function_result)
