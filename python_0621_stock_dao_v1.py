'''
dao means: 'data access object'
stock dao means: this program takes care of accessing stock related info in db
level 4 - UI layer - Web
level 3 - service layer - all your busincess logic
level 2 - entity layer - stock class object / price class object / financial_data class object
level 1 - dao layer - stock dao / price dao / financial_data dao
level 0 - database layer - sqlite3 + dbeaver
'''
import sqlite3

GET_ALL_STOCKS = "select * from stock;"


def connect():
    return sqlite3.connect("../python_0490_database.db")

def get_all_stocks(connection):
    with connection:
        return connection.execute(get_all_stocks).fetchall()


# TEST CODE -------------------------------------

conn = connect()
ret = get_all_stocks(conn)
print(ret)