##################IMPORTANCE###############
# this is how you DEF a var for loop
#you def a var 'i'
# range is a build in function.
#it allows you to generate num within a given range
#range(stop) generates number in range [0,stop)
############################################
print('range (5) generates number from 0-4 and no "5"')
for i in range(5):
    print(i)

print('__________________________________________________________')
##################IMMPORTANCE##############
#STYle 2
#range(start,stop) generates [st,sp)
for i in range (5,10):
    print(i)

print('range(100,100) does not work')
for i in range (100,100):
    print(i)