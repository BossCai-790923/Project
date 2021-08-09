car = {
    "brand": "BMW",
    "model": "X5",
    "year": 2021
}
print(car)

print("access the dictionary in 2 ways ")
car_model = car["model"]
car_year = car["year"]
print(car_model, car_year)

print(car.get("model"), car.get("year"))

print(car.get("price"))  # None
print(car.get("price", "key price does not exist"))  # key price does not exist

# print(car["price"]) # KeyError: "price"


print("in check if key exists in dict ")
if "price" not in car:
    car["price"] = 2000000
print(f"car price is {car['price']}")

print("key 'year' already exists > change value for key 'year'")
car["year"] = 2020
print(car)

print("key 'color' doesn't exist > insert key / value pair into the dictionary")
car["color"] = "red"
print(car)

# important:_______________________________________
# dict keeps items in the same order they were introduced(insertion order) after Python3.7
# _________________________________________________
print("del -> del key/value pair##########################################")
del car["brand"]
print(car)

print("dict -> loop through a dict's key################################")
for key in car:
    print(key, '->', car[key])
# summary: When we you loop through a dict, you are looping through the dict's keys

print(".values() -> Loop through a dict's values ################################")
# print(car.values())
for value in car.values():
    print(value, end=' ')
# summary: use .values() if you want to loop through the dict's values.


print(".keys() -> Loop through a dict's keys ###################################")
for key in car.keys():
    print(key, '->', car[key])
# Summary: 'for key in car.keys():', is the same as 'for key in car:'


print(
    ".items() -> Loop through a dict's items, each item is a tuple, a tuple of key / value pair ########################")
for key, value in car.items():
    print(key, '->', value)
# Summary: .items() gives you a sequence of tuples.


print("-" * 20)
# check dictionary's length
print(f"size of dict car is {len(car)}")

print('pop(key) - remove key / value pair from dictionary ############################')
car_model = car.pop('model')
print(car_model)
print(car)

print('popitem() - remove the last key /value pair from dictionary ####################')
item = car.popitem()
print(item)  # ('color', 'red')
print(car)  # {'year': 2020, 'price': 2000000}

print("clear() - remove all from the dictionary ###################################")
car.clear()
print(car)
