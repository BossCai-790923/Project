

'''
https://leetcode.com/problems/unique-paths/
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
'''

'''
ANALYSIS
---------------------------------------------------------------------------------
Question 1) How to define the dp function? / What's the meaning of the dp array? 
---------------------------------------------------------------------------------
Original Q: How many possible unique paths are there?
Parameterzied the Q: How many possible unique paths are there when the robot is at row n and column m?
f(m,n):
param m : row m
param n : column n
f(m,n)  : total unique path
dp = [i][j]:
index i : row i
index j : column j
dp[i][j]  : total unique path
---------------------------------------------------------------------
Question 2) What's the base case? / How to initialize the dp array?
---------------------------------------------------------------------
dp = np.full([m,n], -1, dtype=np.int32)
[base case]
dp[1] = 1 
dp[:,1] = 1
because, for the 1st column & 1st row, there is only 1 unique path.
------------------------------------------------------------------------
Question 3) What's the state transition? From THE problem to subproblem?
------------------------------------------------------------------------
Because the robot can ony move rightwards and downwards, so for position dp[i][j], the value is:
dp[i][j] = dp[i-1][j] + dp[i][j-1]
'''
import numpy as np


class Solution:

    def uniquePath(self, m: int, n: int) -> int:

        '''
        # Step 1) define dp array -----------------
        dp = np.full([m, n], -1, dtype=np.int32)
        dp[0] = 1
        dp[:,0] = 1
        '''

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        # Step 2) simply loop the 2 states, fill up the dp array using the state transition formula
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # Step 3) return the last value of the dp array
        return dp[m - 1][n - 1]

