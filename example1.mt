Column column1 = Column.new("name1", Integer)
Column column2 = Column.new("name2", String)
Column column3 = Column.new("name3", Float)
Table table1 = Table.new(column1, column2, column3)
value = []
value[0] = 1
value[1] = "String"
value[2] = "hahaha"
Row row1 = Row.new(get_columns(table1), value)
add_row(table1, row1)
