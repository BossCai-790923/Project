# solution1:Create a dict using {}
car = {
    'brand': 'BMW',
    'model': 'X5',
    'year': 2021
}
print(car)

plane = {
    'name': 'boeing787',
    'passenger': 330,
    'cruising_speed': 913,
    'maiden_flight': '15 Dec 2009',
    'wingspan': 60.1,
    'max_speed': 954
}
print(plane)
students={
    1:'tom',
    5:'billy',
    10:'sandy',
    16:'ssssss'
}

print(students)

stock_prices = {
    'dbs': ('d05', 29.710, -0.110, -0.37),
    'singtel': ('z74', 2.380, -0.020, -0.83),
    'uob': ('u11', 26.100, None, None),
}
print(stock_prices)

stupid_dict = {
    'a': 1,
    1: tuple('hello'),
    tuple('hello'): plane
}
print(stupid_dict)

# in summary:
# for key, you can use str / int / float / tuple. BUT YOU CANNOT USE LIST
# for value, you can use anything

# importance !!! ----------------------------------------------------------------------------------------
# you can use immutable value as the dict key.
# in our real life, key can't change it shape. Once key changes its shape, it can't open its lock
# so, you can't use list which is mutable as the dict key
# but for value, you can put anything. Value equals to the 'thing' inside the box which you can use the key to open
# ---------------------------------------------------------------------------------------------------


# solution 2: create a dict using dict constructor ------------------------------------
username_and_age = dict(Peter=38, John=51, Alex=13, Alvin='Unknown')
print(username_and_age)

a_man_list = [('name', 'gumby'),('age', 42)]
a_man_dict = dict(a_man_list)
print(a_man_dict)
print('---------------------------------------------')
# HOMEWORK --------------------------------
# Do not run these code, tell me the output
# Tell me the output of the below code:
# print(stupid_dict['a'])
# print(stupid_dict[stupid_dict['a']])
# print(stupid_dict[stupid_dict[stupid_dict['a']]])

