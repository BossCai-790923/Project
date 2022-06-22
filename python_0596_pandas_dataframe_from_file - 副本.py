
import pandas as pd


'''
Download DBS history price from:
https://finance.yahoo.com/quote/D05.SI/history?p=D05.SI
Step 1) Change Time period to max
Step 2) Press button 'Download'
'''


print("---Create a pandas dataFrame from a csv file ---------------------------")
df1 = pd.read_csv("python_0596_dbs_stock_price.csv")

print("\n\n--Show me first 10 rows ------------------------")
data1 = df1.head(10)
print(data1)

print("\n\n--Show me last 10 rows ------------------------")
data1 = df1.tail(10)
print(data1)

print("\n\n--Show me close price > 37 ------------------------")
data1 = df1[df1.Close > 37]
print(data1)