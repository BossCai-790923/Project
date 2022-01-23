
separate_line = '*~' * 10
print(separate_line)

'''
In python, list are str are quite similar
str is nothing but a list of character
For example, you can:
'''
print(separate_line[0])
print(len(separate_line))

'''
So you can do this with list as well
'''

print('1 dimension list ------------------------')

a = [0] * 5
print(a)

print(id(a[0]))
print(id(a[1]))
print(id(a[2]))


a[2] = 2
print(a)

print('2 dimension list (1) ------------------------')

b = [[0] * 5]
print(b)
'''
explanation:
[0] * 5 is a list which contains 5 zeros
[[0] * 5] is a list which has 1 element only. Its only element is a list which contains 5 zeros.
'''

print(b[0][0])
b[0][1] = 5
print(b)

# b[1] # this is wrong, as b has only 1 value

print('2 dimension list (2) ------------------------')

c = [[0] * 5] * 3
'''
[0] * 5  is a list which contains 5 zeros
[[0] * 5] is a list which has 1 element only. Its only element is a list which contains 5 zeros.
[[0] * 5] * 3  is a list which has 3 elements. The elements are lists which contain 5 zeros.
'''
print(c)

c[0][0] = 1
print(c) # all 3 sublists are updated.

'''
IMPORTANCE!!! ------------------------------
defining 2 dimensions list in this way is wrong.
[[0] * 5] * 3
--------------------------------------------
'''

print('2 dimension list (3) correct! ------------------------')
d = [[0 for i in range(5)] for j in range(3)] # list comprehension inside another list comprehension
print(d)
d[1][1] = 3
print(d)

'''
very ugly, very smelly, not readable at all! 
'''