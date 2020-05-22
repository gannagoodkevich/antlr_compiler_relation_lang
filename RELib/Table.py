class Table:
    def __init__(self, *columns):
        self.columns = []
        self.rows = []
        for column in columns:
            self.columns.append(column)

    def get_columns(self):
        return self.columns

    def add_row(self, row):
        self.rows.append(row)

    def show(self):
        print("-------Table-------")
        columns = "||  "
        for column in self.columns:
            columns += column.name + "." + column.type + "  ||  "
        print(columns)
        rows = '--  '
        for row in self.rows:
            for column in self.columns:
                rows += str(row.info[column.name]) + '  --  '
            rows += '\n--  '
        print(rows)
