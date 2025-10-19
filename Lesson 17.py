import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", timeout=5)


cur = connection.cursor()
print(connection)
print(cur)
cur.execute("DROP TABLE IF EXISTS first_table;") 

cur.execute("CREATE TABLE first_table (name TEXT);")
connection.commit()
connection.close()