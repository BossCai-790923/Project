sp = '____________________________________'
for i in range(10):
    print(i * '*')
print(sp)
for i in range(9):
    print((9-i)*' ' + i * '*')
print(sp)
for i in range(10):
    print(  (10-i)*' ' + i * '*' + (i-1) * '*')

print(sp)
for i  in range(10):
    print((10-i)*' '+ 10 * '*')
print(sp)
for i in range (10):
    print((i-1) *  ' ' + i * '*')
print(sp)
for i in range (10):
    print(((10-i)*2) * ' '+ i*'*')
print(sp)
print('沙漏s 题目')
'''
hourglass
对称图形
' '0,19*
' '1,17*
'''
for i in range(-9,10):
    print(' '*(9-abs(i))+'*'*(abs(i*2)+1))

print(sp)
x=1
for i in range(27):
    if x == 10:
        x=1
    print((10 - x) * ' ' + x * '*' + (x - 1) * '*')
    x+=1
print(sp)
x=1
print('菱形 题目')
'''
19 lines total
' '9,1 *
' '8,3 *
^^^^^^^^^^^
'''
for i in range(-9,10):
    print(' '*abs(i)+'*'*(19-abs(i*2)))