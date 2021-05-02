'''
Requirement:
Find all the possible value for number X which satisfies the following condition:
1) X + 100 is a square number.
2) X + 100 + 168 is another square number.

X is in range [-100, 2000]
HINT: We introduce an alogrithm to check whether a number is a square number in program 0022.
'''
'''
code logic
Try check x is(not)SQ
200+100+168<2500
2sq.num is all less than 50
'''
import math
for i in range (1,51):
    sq1=i**2
    sq2=sq1+168

    sqr_rt_2 = math.sqrt(sq2)
    sqr_rt_2_int=int(sqr_rt_2)
    if sqr_rt_2_int != sqr_rt_2:
        continue
    print(sq1-100,'is that number')
