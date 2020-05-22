#!/usr/bin/python3

from RELib.Column import Column
from RELib.Row import Row
from RELib.Table import Table

def func1(a, b):
	table2 = Table(a, b)
	var = "World"
	value1 = []
	value1.insert(0, "Hello")
	value1.insert(1, var)

	row2 = Row(table2.get_columns(), value1)
	table2.add_row(row2)
	table2.show()
	ant = 10
	return row2
lalala = 2.00
asr = "Hello World"
new_str = str(200)
column1 = Column("name1", "Integer")
column2 = Column("name2", "String")
table1 = Table(column1, column2)
value = []
value.insert(0, 1)
value.insert(1, "hahaha")

row1 = Row(table1.get_columns(), value)
table1.add_row(row1)
table1.show()
func1(column2, column1)
for i in range(0, 5):
	value2 = []
	value2.insert(0, i)
	value2.insert(1, "and what")

	row3 = Row(table1.get_columns(), value2)
	table1.add_row(row3)
	new_s = str(200)
	new_s += str(200)
table1.show()
if lalala < 2:
	func1(column1, column2)
else:
	lalala = 900
