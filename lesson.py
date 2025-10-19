import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", timeout=5)
cur = connection.cursor()

print(connection)
print(cur)

connection.close()