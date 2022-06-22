import pandas as pd
import sqlite3

print("---Create a pandas dataFrame from a csv file ---------------------------")
df1 = pd.read_csv("python_0596_dbs_stock_price.csv")

print("---Insert dataFrame data into database ---------------------------")
conn = sqlite3.connect("../PYTHON CLASS 01/python_0480_database_soccer.sqlite")
df1.to_sql("dbs_stock_prices", conn, if_exists="replace")


'''
Then you can directly run these sql in dbeaver: 
select * from dbs_stock_prices dsp;
select count(*) from dbs_stock_prices dsp ;
select min(close), max(close), avg(close) from dbs_stock_prices dsp where Date > '2020-01-01' and Date < '2020-12-31';
select min(close), max(close), avg(close) from dbs_stock_prices dsp where Date > '2021-01-01' and Date < '2021-12-31';
select min(close), max(close), avg(close) from dbs_stock_prices dsp where Date > '2022-01-01';
'''