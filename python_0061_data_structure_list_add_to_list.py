fruits =['apple','orange','banana','pear']
animals=['tiger','elephant','snake','shark']
##1 use append-add  a new value to the end of the list
fruits.append('watermalon')
print(fruits)
## list canbe 混搭
fruits.append(True)
fruits.append(1)
fruits.append(1.2)
fruits.append([1,2,3])
print(fruits)
'''
       ['tiger', 'elephant', 'snake', 'shark']
index  0           1         2        3   
        -4         -3         -2      -1
'''
##2 use insert -add a new value to the lust at index specified
animals.insert(1,'leopard')
print(animals)
animals.insert(100,'giraffe')
print(animals)
animals.insert(-2,'hedgehog')
print(animals)
##3 use extend -join anotherlist
insects=['caterpillar','fly','ant']
animals.extend(insects)
print(animals)


##4 use + to join another list
birds = ['swallow','eagle','toucan']
animals+=birds
print(animals)

many_birds = birds*3
print(many_birds)

zero_list = [0]*100
print(zero_list)


