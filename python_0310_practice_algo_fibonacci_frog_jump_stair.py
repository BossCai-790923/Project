'''
Requirement:
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
1 -> 1
2 -> 2
3 -> 3
'''


def fib(n):
    if n <= 1:
        return 1
    dp = []
    for i in range(n+1):
        dp+=[1]
    for i in range(2, n + 1):
        dp[i] =dp[i - 1] + dp[i - 2]
    return dp[n]

input=int(input(' : '))
print(fib(input))