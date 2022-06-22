# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        nums.sort()

        j = 0
        for i in range(len(nums)):
            if nums[i] < 0 and j < k:
                nums[i] = -nums[i]
                j += 1
            else:
                break
        if j == k:
            return sum(nums)
        l = k - j  
        if l % 2 == 0:
            return sum(nums)
        nums.sort()
        nums[0] = -nums[0]
        return sum(nums)



