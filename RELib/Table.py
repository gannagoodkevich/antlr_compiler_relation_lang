class Table:
    def __init__(self, *columns):
        self.columns = []
        self.rows = []
        for column in columns:
            self.columns.append(column)

    def get_columns(self):
        print("Get columns")
        return self.columns

    def add_row(self, row):
        print("Add row")
        self.rows.append(row)
