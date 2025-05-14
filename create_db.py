import sqlite3 as sql

con = sql.connect('db_web.db')
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS users ")

# Create users table
sql = '''CREATE TABLE "users" (
     "UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"UNAME"	TEXT NOT NULL,
	"CONTACT"	TEXT NOT NULL
    )'''

cur.execute(sql)

con.commit()
con.close()
