#!/usr/bin/python3

lalala = 2.00
asr = "Hello World"
new_str = str(200)
column1 = Column("name1", "Integer")
column2 = Column("name2", "String")
table1 = Table(column1)
value = []
value[0] = 1
value[1] = asr
value[2] = "hahaha"

row1 = Row(table1.get_columns(), value)
table1.add_row(row1)
func1(column1, column2)
for i in range(0, 20):
	table1.add_row(row1)
	new_s = str(200)
	new_s += str(200)
if lalala < 2:
	func1(column1, column2)
else:
	lalala = 900
def func1(a, b):
	table1 = Table()
	value1 = []
	value1[0] = 200

	row1 = Row(table1.get_columns(), value)
	ant = 10
	return row1
