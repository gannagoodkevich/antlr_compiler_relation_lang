class AstArray:
    def __init__(self):
        self.name = ''
        self.elements = []
        self.indexes = []

    def print_info(self):
        print("Name:")
        print(self.name)
        print("Elements:")
        print(self.elements)
        print("Indexes:")
        print(self.indexes)
