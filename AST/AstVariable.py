class AstVariable:
    def __init__(self):
        self.name = ""
        self.operator = ""
        self.value = []

    def print_info(self):
        print("Var name:")
        print(self.name)
        print("Operator:")
        print(self.operator)
        print("Value:")
        print(self.value)
