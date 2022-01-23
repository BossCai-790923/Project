'''
leetcode 322

https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 10^4
'''

'''
---------------------------------------------------------------------------------
Question 1) How to define the dp function? / What's the meaning of the dp array? 
---------------------------------------------------------------------------------

The Q: What is the fewest number of coins that you need to make up that amount i? 

f(n): 
param n: amount n
f(n)   : the min coins count

So our dp array:
dp = []
index i: amount n
dp[i]  : the min coins count


---------------------------------------------------------------------
Question 2) What's the base case? / How to initialize the dp array?
---------------------------------------------------------------------
dp = [10001] * (amount + 1)
dp[0] = 0

------------------------------------------------------------------------
Question 3) What's the state transition? From THE problem to subproblem?
------------------------------------------------------------------------

Let's assume, it is given 3 denominations - 1 / 2 / 5

case 1: the last coin used is 1
total coins is: dp[i-1] + 1

case 2: the last coin used is 2
total coins is: dp[i-2] + 1

case 3: the last coin used is 5
total coins is: dp[i-5] + 1

so:
dp[i] = min(dp[i-1]+1, dp[i-2]+1, dp[i-5]+1)

'''

class Solution:

    def coinChange(self, coins: list[int], amount: int) -> int:

        # define dp array ------------------------------
        dp = [10001] * (amount + 1)
        dp[0] = 0

        # fill up dp array ----------------------------
        # loop the only state - amount:
        for i in range(1, amount+1):
            cases = []
            for c in coins:
                if i - c >= 0:
                    cases.append(dp[i-c] + 1)
                else:
                    cases.append(10001)
            dp[i] = min(cases)

        if dp[amount] >= 10001:
            return -1

        return dp[amount]

s = Solution()
answer = s.coinChange([1,2,5], 11)
print(answer)

# class Solution:
#
#     def coinChange(self, coins: list[int], amount: int) -> int:
#
#         dp = [float("inf")] * (amount + 1)
#         dp[0] = 0
#
#         for i in range(1, amount+1):
#             dp[i] = min(dp[i-c] if i - c >= 0 else float("inf") for c in coins) + 1
#
#         return dp[-1] if dp[-1] != float("inf") else -1