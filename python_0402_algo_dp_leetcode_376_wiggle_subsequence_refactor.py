'''
https://leetcode.com/problems/wiggle-subsequence
LWS - Longest Wiggle Subsequence
LIS - Longest Increasing Subsequence
------------------------------------------------------------------------------
Question 1) How to define the dp function? / What's the meaning of the dp array?
------------------------------------------------------------------------------
Original Q      :  return the length of the LWS of nums.
Parameterize Q  :  return the length of the LWS of nums till index n.
f(n):
param n : index n of array nums
f(n)    : the length of the LWS of nums till index n.
dp array.
Character 1)
For each number in nums, there are 2 types of Wiggle Subsequences.
Let's say the last 2 numbers of WS is a and b.
Type 1) Up WS. When a < b
Type 2) Down WS. When a > b
Character 2)
When you append a number to Up WS, then it becomes Down WS
When you append a number to Down WS, then it becomes Up WS
Because a Up/Down WS was Down/Up WS, so there max diff is always 0 or 1.
Becase each number has 2 LWS, up and down.
index i      index i of array nums.
dp_up[i]     len(Up LWS) for array nums' head array till index i
dp_down[i]   len(Down LWS) for array nums' head array till index i
---------------------------------------------------------------------
Question 2) What's the base case? / How to initialize the dp array?
---------------------------------------------------------------------
dp_up = [0] * len(nums)
dp_down = [0] * len(nums)
dp_up[0] = 1
dp_down[0] = 1
------------------------------------------------------------------------
Question 3) What's the state transition? From THE problem to sub-problem?
------------------------------------------------------------------------
for index i
if nums[i] > nums[i-1]  -> dp_down[i] = dp_up[i-1] + 1
                           dp_up[i] = dp_up[i-1]
if nums[i] == nums[i-1]  -> dp_down[i] = dp_down[i-1]
                           dp_up[i] = dp_up[i-1]
if nums[i] < nums[i-1]  -> dp_up[i] = dp_down[i-1] + 1
                           dp_down[i] = dp_down[i-1]
'''

class Solution:
        # Step 3) simply loop the state, fill up the dp array using the state transition formula

    def wiggleMaxLength(self, nums: list) -> int:

        dp_up = 1
        dp_down = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp_down = dp_up + 1
            elif nums[i] < nums[i-1]:
                dp_up = dp_down + 1

        max(dp_up, dp_down)