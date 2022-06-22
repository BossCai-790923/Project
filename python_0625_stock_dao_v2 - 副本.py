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
from python_0623_stock_entity import stock




GET_ALL_STOCKS = "select * from stock;"

GET_STOCK_BY_ID = "select * from stock where id = ?;"

GET_STOCK_BY_TICKER = "select * from stock where ticker = ?;"

GET_STOCK_BY_NAME = "select * from stock where name = ?;"







def connect():
    return sqlite3.connect("../program6/python_0490_database.db")


def get_all_stocks(connection):
    with connection:
        tup_list = connection.execute(GET_ALL_STOCKS).fetchall()
        stock_list = [stock(*t) for t in tup_list]
        return stock_list


def get_by_id(connection, id):
    with connection:
        tup = connection.execute(GET_STOCK_BY_ID, (id,)).fetchone() # single value tuple must use comma

        if tup == None:
            return None

        s = stock(*tup)
        return s

'''
HOMEWORK:
Implement below 2 methods:
1) you need to add 2 sqls in the front of the files. Please revise 480
2) You need to mimic function get_by_id() to implement these 2 methods.
'''

def get_by_ticker(connection, ticker):
    with connection:
        tup = connection.execute(GET_STOCK_BY_TICKER, (ticker,)).fetchone() # single value tuple must use comma

        if tup == None:
            return None

        s = stock(*tup)
        return s


def get_by_name(connection, name):
    with connection:
        tup = connection.execute(GET_STOCK_BY_NAME, (name,)).fetchone() # single value tuple must use comma

        if tup == None:
            return None

        s = stock(*tup)
        return s




# TEST CODE -------------------------------------

def print_menu():
    menu = '''
    --------------------------
    Please give me a int value:
    1) get all stocks
    2) get stock by id
    3) get stock by ticker
    4) get stock by name
    5) exit
    '''
    print(menu)


'''
HOMEWORK2:
Finish my half-done code below
'''

if __name__ == "__main__":

    conn = connect()

    while True:

        print_menu()

        command = int(input())

        if command == 1:
            stock_list = get_all_stocks(conn)
            print(stock_list)

        elif command == 2:
            id = int(input("ID: "))
            stock = get_by_id(conn, id)
            print(stock)

        elif command == 3:
            ticker = input("Ticker: ")
            stock = get_by_ticker(conn, ticker)
            print(stock)

        elif command == 4:
            name = input("Name: ")
            stock = get_by_name(conn, name)
            print(stock)

        elif command == 5:
            exit()

        else: # 兜底
            print(f"Unrecognized command: {command}")










    # ret = get_all_stocks(conn)
    # print(ret)
    #
    # stock = get_by_id(conn, 1)
    # print(stock)