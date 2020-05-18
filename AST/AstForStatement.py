class AstForStatement:
    def __init__(self):
        self.var = ""
        self.start_value = []
        self.end_value = []
        self.expressions = []

    def print_info(self):
        print("Var iterator:")
        print(self.var)
        print("Start:")
        print(self.start_value)
        print("End:")
        print(self.end_value)
        print("Expressions:")
        print(self.expressions)
