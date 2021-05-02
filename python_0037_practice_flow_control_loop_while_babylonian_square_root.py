'''
B.S-r. a. is very famous???
here is how it works

001 def var a=1
002 def var b = x / a

003 assign var a = (a+b)/2
004 assign var b = x/a

because sq.rt * sq.rt = x,so a and b one is smaller than sq.rt
another is bigger than sq.rt
we move a to the mid point between a and b
and a*b = x if a closer to sq.rt, b is closer to sq.rt
repeat________________________
005 ass var a = (a+b)/2
006 ass var a  = (a+b)/2
repeat ________________________

until a is close enough, say b - a <0.00000000000001
then a is eaqual to b(almost)
then a or b is the sq.rt of x
'''
diff = 0.0000000000000000000000000000000000000000000000000000000000000000000000001
x = int(input('number:'))
#defintial value
a = 1
b = x / a
actual_diff = b - a
print(f'a:{a},b:{b}.actual diff:{actual_diff}')
while actual_diff > diff:
    a = (a+b)/2
    b = x/a

    actual_diff = abs(a-b)
    print(f'a:{a},b:{b}.actual diff:{actual_diff}')

print(f'square root of {x} is {a}')
print(f'{a} * {a} = {a ** 2}')
