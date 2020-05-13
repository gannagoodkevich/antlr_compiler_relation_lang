class AstColumnAssignment:
    def __init__(self):
        self.var = ""
        self.type = ""
        self.column_name = ""
        self.params = []

    def print_info(self):
        print("Var name:")
        print(self.var)
        print("Column type:")
        print(self.type)
        print("Column name:")
        print(self.column_name)
        print("Params:")
        print(self.params)
