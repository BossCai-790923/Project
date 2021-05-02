'''
Requirement:
There are 4 numbers: 1/2/3/4.
List out all 3 digits numbers using these 4 numbers.
You cannot use the same number twice in the 3 digits numbers.
'''

#1 how to generate 1 digit number?
for i in range (1,5):
    print(i,end=' ')

print('\n_____________________________')
#2 how to generate 2 digit number?
for i in range(1,5):
    for j in range(1,5):
        num = i*10 + j
        print(num,end=' ')
print('\n_____________________________')
#3 how to generate 3 digit number?
for i in range(1,5):
    for j in range(1,5):
        for x in range(1,5):
            num = i*100 + j*10 + x
            print(num,end=' ')
print('\n_____________________________')
#4 没有一个数位相同:
for i in range(1,5):
    for j in range(1,5):
        for x in range(1,5):
            if i != j and i != x and j != x:
                num = i*100 + j*10 + x
                print(num,end=' ')



