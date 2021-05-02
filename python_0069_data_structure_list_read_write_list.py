fruits = ['apple','orange','banana','pear']
animals = ['tiger','elephant','snake','shark']
#_____________________________________
#read item value from list
#_____________________________________
##1)use square bracket
print(animals[0],'is at index 0')
print(animals[-1],'is at index -1')
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

##2)use for loop
for animal in animals:
    print(animal,end = ' ')

print('\n____________________________')
#_______________________________-
#read item index from list/
#_______________________________-
##1 use index() method
print('tiger index :',animals.index('tiger'))
print('shark index :',animals.index('shark'))

#############################################
#read ITEM index/value from the list        #
#############################################
##1)
index=0
for animal in animals:
    print(f'{index}:{animals}')
    index+= 1

#importance____________________________:
for index,animal in enumerate(animals):
    print(index,';',animals)
#importance____________________________:
#built in function enmuerate(animals)combines index and value into one group

# write to list
    #write means change/update value inside the list

animals[0]='shark'
print(animals)
fruits[1]='durian'
print(fruits)
##############################
#remember:list is mutable!!!!#