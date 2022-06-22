import sqlite3

CREATE_PRICE_TABLE = '''
drop table if exists price;
create table price (
    id integer not null primary key,
    stock_id integer, 
    trade_date text,
    open real,
    high real,
    low real,
    close real,
    turnover_by_volume integer, -- 成交量, how many shares have been traded for the day
    turnover_by_value integer,  -- 成交额, how much money have been traded for the day
    change_rate real            -- 换手率, traded shares / total shares
);
'''

def connect():
    return sqlite3.connect("../python_0490_database.db")

def create_price_table(conn):
    conn.executescript(CREATE_PRICE_TABLE)

# TEST CODE ------------------------

if __name__ == "__main__":
    conn = connect()
    create_price_table(conn)