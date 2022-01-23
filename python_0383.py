
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        '''
        1) as this is a step-by-step strategy, I need to loop all those numbers one by one.
        2) I keep a sub_array, and I try to keep sum(sub_array) as big as possible
        3) whenever sum(sub_array) becomes smaller, I try to save the current sum(sub_array) into a possible_result list.
        '''

        sub_array = []
        largest_sum = float("-inf")

        sub_array_sum = 0

        for i in nums:

            if i < 0 and len(sub_array) > 0 and sub_array_sum > largest_sum:
                    largest_sum = sub_array_sum

            if sub_array_sum <= 0:
                sub_array.clear()
                sub_array_sum = 0

            sub_array.append(i)
            sub_array_sum += i

        if len(sub_array) > 0 and sub_array_sum > largest_sum:
            largest_sum = sub_array_sum

        return largest_sum

