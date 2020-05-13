class AstRowAssignment:
    def __init__(self):
        self.var = ""
        self.table = []
        self.row_vars = ""
        self.params = []

    def print_info(self):
        print("Var name:")
        print(self.var)
        print("Table:")
        print(self.table)
        print("Row values:")
        print(self.row_vars)
        print("Params:")
        print(self.params)
