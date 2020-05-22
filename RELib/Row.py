class Row:
    def __init__(self, columns, values):
        self.row = {}
        if len(columns) == len(values):
            for value in values:
                column = columns[values.index(value)]
                row[columnn.name] = value
