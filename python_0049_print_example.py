#by def,print() inserts a spave betwen the itmes it prints.
#U can change this by using a sep. parameter
print(1,2,3)
print(1,2,3,sep='-')
print(1,2,3,sep='_-*-_')
print(1,2,3,sep='\n')

print('_-*-__-*-__-*-__-*-__-*-__-*-__-*-__-*-__-*-__-*-__-*-__-*-__-*-__')

#by def,print() add a \n to change line
#U can change this by using a ending parameter

for i in range(5):
    print(i)
print('_______________________________________')

for i in range(5):
    print(i,end = ' ')