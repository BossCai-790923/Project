# https://leetcode.com/problems/longest-increasing-subsequence/

'''
------------------------------------------------------------------------------
Question 1) How to define the dp function? / What's the meaning of the dp array?
------------------------------------------------------------------------------
Original Q      : What is the length of LIS of array nums?
Parameterized Q : What is the length of LIS of array nums' head array till index n? Extra condition: nums[n] should be the end of the LIS.
f(n):
param n: index n of array nums
f(n)   : len(LIS) of array nums' head array till index n? Extra condition: LIS ends at nums[n]
We need to calculate till f(len(nums)-1)
So our dp array:
dp = []
index i : index i of array nums
dp[i]   : en(LIS) of array nums' head array till index i
---------------------------------------------------------------------
Question 2) What's the base case? / How to initialize the dp array?
---------------------------------------------------------------------
nums[i] itself can be a single number LIS, so
dp = [1] * len(nums)
------------------------------------------------------------------------
Question 3) What's the state transition? From THE problem to sub-problem?
------------------------------------------------------------------------
For example:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums[0]=10  f(0)=1
nums[1]=9   f(1)=1
nums[2]=2   f(2)=1
nums[3]=5   f(3)=2  because: 1) 5 can be appended after nums[2]
                             2) f(2)=1
                    so: f(3) = f(2) + 1 = 2
nums[4]=3   f(4)=2  because: 1) 3 can be appended after nums[2]
                             2) f(2)=1
                    so: f(4) = f(2) + 1 = 2
nums[5]=7   f(5)=3  because: 1) 7 can be appended after nums[2] - 2
                             2) f(2)=1
                    so: f(5) = f(2) + 1 = 2
                    because: 1) 7 can be appended after nums[3] - 5
                             2) f(3)=2
                    so: f(5) = f(3) + 1 = 3
                    because: 1) 7 can be appended after nums[4] - 3
                             2) f(4)=2
                    so: f(5) = f(4) + 1 = 3
                    So, let's choose 1 biggest number among {2,3}, which is 3
Conclusion:
dp[i] = max(dp[j])+ 1    condition: 0 <= j < i   and nums[j] < nums[i]
-------------
final answer
-------------
max(dp[i])
'''
from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        # init dp array
        dp = [1] * len(nums)

        # loop the only state - index i
        for i in range(1, len(nums)):

            for j in range(i):

                if nums[i] > nums[j]: # if : nums[i] can be appended after nums[j]
                    dp[i] = max(dp[i], dp[j] + 1)

        print(dp)

        return max(dp)


# test program --------------------------

if __name__ == '__main__':

    s = Solution()

    answer = s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])

    print(answer)