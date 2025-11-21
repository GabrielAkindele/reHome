import sqlite3
import hashlib


conn = sqlite3.connect("db/rehome.db")

cursor = conn.cursor()

password = hashlib.sha256("admin123".encode()).hexdigest()

results = cursor.execute("select * from items where category = ? ",(None,)).fetchall()



print(results)

conn.commit()
conn.close()