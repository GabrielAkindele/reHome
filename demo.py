import sqlite3

# from werkzeug.security import generate_password_hash


conn = sqlite3.connect("db/rehome.db")

cursor = conn.cursor()

# hashed = generate_password_hash("group")

Search = "Groceries"
items = cursor.execute(
    "SELECT items.*, users.name AS owner_name "
    "FROM items JOIN users ON items.user_id = users.id "
    "WHERE category like ? "
    "ORDER BY items.created_at DESC",
    ("{}%".format(Search),),
).fetchall()


print(items)

conn.commit()
conn.close()
