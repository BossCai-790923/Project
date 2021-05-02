# -----------------------------------------------------------
# What is memory address?
# 1 memory card is like a city.
# 1 byte is a family.
# each byte has an address, Just like your family has an address.
# Memory address points to some byte, or the beginning of several bytes.
# -----------------------------------------------------------

# The variable is a pointer, it points to a box.
# Depends on the variable type and value, it takes up different size of bytes.
# id() function: return the variable's box first byte memory address.

a=[1,2,3]
print(id(a))
b=[4,5,6]
print(id(b))
print('____________________________________')
b=a
print(id(b))
#value equality
print('a=b:',a==b)#True
#identity equality
print('a is b:',a is b)#True
print('____________________________________')
c=[1,2,3]
print(id(c))
print('a=c',a==c)#True
print('a is c',a is c)#False

print('_________________________________')
x=10
print(id(x))
x+=2
print(id(x))
print('___________________________________')