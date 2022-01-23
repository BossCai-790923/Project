
'''
-------------
Analysis
-------------
rectangle m * n
The robot takes
1) m-1 steps rightwards
2) n-1 steps downwards
In total, it takes m + n - 2 steps
Let's assume there are 7 rightwards steps: a b c d e f g
Let's assume there are 3 downwards steps: 1 2 3
So this equals to randomly pick 3 spaces for downwards steps in a 10 spaces
a b 1 c 2 d e f 3 g
- - - - - - - - - -
So, according to Combination formula:
C(n,k) = n!/(k! * (n-k)!)
The answer is :
factorial(m+n-2) / (factorial(m-1) * factorial(n-1))
"permutation and combination" Reference:
https://zhuanlan.zhihu.com/p/41855459
https://www.youtube.com/watch?v=XJnIdRXUi7A
'''
#
# from math import factorial
#
# class Solution:
#     def uniquePath(self, m:int, n:int) -> int:
#         return factorial(m + n - 2) // (factorial(m-1) * factorial(n-1))


