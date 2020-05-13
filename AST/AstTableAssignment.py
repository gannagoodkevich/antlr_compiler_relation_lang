class AstTableAssignment:
    def __init__(self):
        self.var = ""
        self.columns = []

    def print_info(self):
        print("Var name:")
        print(self.var)
        print("Columns:")
        print(self.columns)
