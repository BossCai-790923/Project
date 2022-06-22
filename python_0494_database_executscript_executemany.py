import sqlite3

with sqlite3.connect("python_0490_database.db") as conn:
    cursor = conn.cursor()

    cursor.executescript(
        """
        drop table if exists people;
    
        create table people (
            firstname text,
            lastname text,
            age int
        );
    
        insert into people values ('Ron', 'Liu', 42);
        """
    )
    '''
    IMPORTANCE!! -------------------
    cursor.executescript(your_sql_script): run your sql script(multiple sqls separated by ;)
    -------------------------------------------------
    '''

    people_values = (
        ('Tom', 'Liu', 20),
        ('Billy', 'Zhang', 22),
        ('Sue', 'Wang', 26)
    )
    cursor.executemany("insert into people values (?,?,?)", people_values)
    '''
    IMPORTANCE!! ---------------------------------------------------------------------
    cursor.executemany("your_sql_template", param_tuple): run your sql insert with multiple records
    -------------------------------------------------------
    '''

    cursor.execute('select * from people')
    result = cursor.fetchall()
    print(result)