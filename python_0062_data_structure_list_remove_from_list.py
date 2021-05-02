animals=['tiger','elephant','snake','shark']*2
print(animals)
##1 del -remove by index
del animals[1]
print(animals)
##2 pop-pop by index
#pop returns the popped item
popped_animal = animals.pop()
print(popped_animal,'is popped out')
print(animals)

popped_animal = animals.pop(1)
print(popped_animal,'is popped out as index 1')
print(animals)

#Index error:pop index out of range

#check before calling!!!!!!
index = 20
if 0 <= index < len(animals):
    popped_animal = animals.pop(index)
    print(popped_animal, 'is popped out.')
    print(animals)
else:
    print(f"{index} is an invalid value for list animals. Right now we only have {len(animals)} items in animals list.")

##3 remove-by value
animals.remove('tiger')
print(animals)
if 'leopard'in animals:
    animals.remove('leopard')
else:
    print('leopard does not exist in list animals')
    print(animals)



