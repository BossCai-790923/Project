import pandas as pd

print("--Create DataFrame from some our own custom data ----------------------")

df1 = pd.DataFrame({

    "name" : ["Tom", "Billy", "Sandy", "Sue", "Olivia"],
    'gender' : ['M', 'M', 'M', "F", 'F'],
    "age" : [15, 13, 11, 12, 16],
    "class" : [1, 2, 2, 1, 2]

})

print(df1)


print("\n\n---Show me even lines (Use slice) -------------------")
print(df1[::2])

print("\n\n---Show me column names -------------------")
print(df1["name"])

print("\n\n---Show me line 2 -------------------")
print(df1.loc[1])

print("\n\n---Show me rows with age greater than 12 -------------------")
print(df1[df1.age > 12])

print("\n\n---Show me all the boys -------------------")
print(df1[df1.gender == 'M'])


print("\n\n---Rename colum name -------------------")
df1.rename(columns={'name':"Name", 'gender':'Gender', 'age': 'Age', 'class':"Class"}, inplace=True)
print(df1)