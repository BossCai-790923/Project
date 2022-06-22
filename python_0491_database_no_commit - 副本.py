import sqlite3


# Step 1) insert data without commit ------------------------------

conn = sqlite3.connect("python_0490_database.db")

cursor = conn.cursor()

cursor.execute("drop table if exists user")

cursor.execute('''
create table user(
    id int primary key,
    username text not null,
    password text not null
)
''')

cursor.execute("insert into user values (1, 'Tom', '123')")
cursor.execute("insert into user values (2, 'Billy', 'qwe')")
cursor.execute("insert into user values (3, 'Sandy', 'ert')")

conn.commit()
conn.close()



# Step 2) query data ----------------


conn = sqlite3.connect("python_0490_database.db")

cursor = conn.cursor()

cursor.execute("select * from user")
for row in cursor.fetchall():
    print(row)

conn.close()