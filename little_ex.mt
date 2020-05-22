def func1(a,b,c)

Integer lalala = (Integer) 2.00
String asr = "Hello World"
String new_str = (String) 200

Column column1 = Column.new("name1", Integer)
Column column2 = Column.new("name2", String)
Table table1 = Table.new(column1, column2)
value = []
value[0] = 1
value[1] = "hahaha"
Row row1 = Row.new(get_columns(table1), value)
add_row(table1, row1)
show(table1)
func1(column2, column1)

for(i = 0; i < 5; i+=1)
  value2 = []
  value2[0] = i
  value2[1] = "and what"
  Row row3 = Row.new(get_columns(table1), value2)
  add_row(table1, row3)
  String new_s = (String) 200
  new_s += (String) 200
end

show(table1)

if lalala < 2
  func1(column1, column2)
else
  lalala = 900
end

def func1 (a,b)
  Table table2 = Table.new(a, b)
  String var = "World"
  value1 = []
  value1[0] = "Hello"
  value1[1] = var
  Row row2 = Row.new(get_columns(table2), value1)
  add_row(table2, row2)
  show(table2)
  Integer ant = 10
  return row2
end
