class Row:
    def __init__(self, columns, values):
        self.info = {}
        if len(columns) == len(values):
            for value in values:
                column = columns[values.index(value)]
                self.info[column.name] = value
        else:
            print("Error: column value is not matching")
