
# https://leetcode.com/problems/lemonade-change/
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        money = {5:0, 10:0}

        for bill in bills:

            # case 1
            if bill == 5:
                money[5] += 1

            # case 2
            elif bill == 10:
                money[10] += 1
                money[5] -= 1
                if money[5] < 0:
                    return False

            # case 3
            else:
                money[5] -= 1
                if money[5] < 0:
                    return False

                if money[10] > 0:
                    money[10] -= 1
                elif money[5] > 1:
                    money[5] -= 2
                else:
                    return False

        return True