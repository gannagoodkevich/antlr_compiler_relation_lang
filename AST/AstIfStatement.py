class AstIfStatement:
    def __init__(self):
        self.var = []
        self.condition = []
        self.operator = ""
        self.if_expressions = []
        self.else_expressions = []

    def print_info(self):
        print("Var condition:")
        print(self.var)
        print("Operator:")
        print(self.operator)
        print("Condition value:")
        print(self.condition)
        print("Expressions in if:")
        print(self.if_expressions)
        print("Expressions in else:")
        print(self.else_expressions)
