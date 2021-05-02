import math
def square(x):
    '''
    this will return a square-number of X.
    :param x: X
    :return: Sq Number
    '''
    return x**2
result1=square(1)
result2=square(2)
print(result2,result1)
result=[]
for i in range(101):
    result.append(square(i))
print(result)

def volume_of_cuboid(L,W,H):
    return L*W*H
l=5
w=4
h=3
print('Lenth>',l,'width>',w,'height>',h,volume_of_cuboid(l,w,h))
def nthroot(x,n):
    i=x**(1/n)
    print(i)
nthroot(625,3)
nthroot(625,2)
nthroot(4,2)