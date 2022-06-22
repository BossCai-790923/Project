import sqlite3

'''
Q) Why should we use sql template?
A) Sql template can enhance database performance greatly.
   Sql template allows database server to parse / validate / generate execution plan only ONCE.
   Next time, you send over the same sql template to database server, database server doesn't need to redo the job. 
'''


# with sqlite3.connect(":memory:") as conn:
with sqlite3.connect("python_0490_database.db") as conn:

    cursor = conn.cursor()
    cursor.execute("create table lang(name, first_appeared)")

    '''
    Solution 1) Use question mark in your sql template ---------------------------
    '''

    cursor.execute("insert into lang values(?, ?)", ("C", 1972))
    '''
    insert into lang values (?, ?)    is a sql template, it contains 2 placeholders. It expects you to replace the 2 ? with 2 actual values.
    ("C", 1972)                       is the actual values which you replaces the 2 ? with.
    '''

    lang_list = [
        ("Fortran", 1957),
        ("Python", 1991),
        ("Go", 2009)
    ]
    cursor.executemany("insert into lang values(?, ?)", lang_list)



    '''
    Solution 2) Use named-parameters in your sql template ----------------------- 
    '''
    cursor.execute("select * from lang where first_appeared=:year", {"year":1972})
    result = cursor.fetchall()
    print(result)
