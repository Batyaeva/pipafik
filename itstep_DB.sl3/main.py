import sqlite3
connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=3;")
connection.commit()
cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()