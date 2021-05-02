'''
Requirement:
Find all the possible value for number X which satisfies the following condition:
1) X + 100 is a square number.
2) X + 100 + 168 is another square number.

X is in range [-100, 2000]
HINT: We introduce an alogrithm to check whether a number is a square number in program 0022.
'''
import math
x=0
y=0
rt=0
for i in range(-100,2001):
    sq1=i+100
    sq2=sq1+168
    sq1_rt=math.sqrt(sq1)
    sq1_rt_int=int(sq1_rt)
    if sq1_rt != sq1_rt_int:
        continue
    sq2_rt=math.sqrt(sq2)
    sq2_rt_int=int(sq2_rt)
    if sq2_rt != sq2_rt_int:
        continue
    print(i,'is that number')


