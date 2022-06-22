import sqlite3



# Step 1) connect to a sqlite database
conn = sqlite3.connect("python_0490_database.db")
'''
if the sqlite database file python_0490_database.db doesn't exist,  this code will create a new database.
You can use a special name as below
conn = sqlite3.connect(":memory:")
This will create a in-memory database, when your program exits, the database is gone as well.
'''


# Step 2) get cursor
cursor = conn.cursor()
'''
Q) What is cursor?
A) cursor is the GATEWAY object you use to interact with database.
   you use cursor to run select / update / delete / insert sqls.
   you use cursor to run drop table / create table sqls.
'''


# drop table if exists
cursor.execute("drop table if exists user")
'''
IMPORTANCE!! -------------------------------
cursor.execute(your_sql): run a single sql
--------------------------------------------
'''


#create table
cursor.execute('''
create table user(
    id int primary key,
    username text not null,
    password text not null
)
''')


# insert data
cursor.execute("insert into user values (1, 'Tom', '123')")
cursor.execute("insert into user values (2, 'Billy', 'qwe')")
cursor.execute("insert into user values (3, 'Sandy', 'ert')")


# save the data
conn.commit()
'''
IMPORTANCE!! ---------------------------------------------------------------------------------------------------------
conn.commit(): after you modify the data - insert / update / delete, you need to commit your changes to the database
----------------------------------------------------------------------------------------------------------------------
'''


print("cursor.fetchall() example 1 ------------------------------------------------------------")

# select
cursor.execute("select * from user")
result = cursor.fetchall() # returns a list of tuple
'''
IMPORTANCE!! ---------------------------------- 
conn.fetchall(): get result of your select sql
-----------------------------------------------
'''
# print(result)
for row in result:
    print(row)


print("cursor.fetchall() example 2 ------------------------------------------------------------")

# select
cursor.execute("select * from user")
for row in cursor.fetchall():
    print(row)



print("cursor.fetchone() ------------------------------------------------------------")

cursor.execute("select count(*) from user")
result = cursor.fetchone() # returns a single tuple
print(result)


conn.close()
'''
IMPORTANCE!! ---------------------------------- 
conn.close(): close the db connection
-----------------------------------------------
'''