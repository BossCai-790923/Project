'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/
------------
Logic
------------
Infix Notation
(2 + 3) * 4
Postfix Notation
2 3 + 4 *
Rule 1: When I see operand, I push to stack
Rule 2: When I see operator, I pop twice, and do the simple calculation
push 2
push 3
pop 3
pop 2
caculate 2 * 3 = 6
push 6
push 4
pop 4
pop 6
calculate 4 * 6 = 24
push 24
pop2 24 -> final result
'''

from typing import List

class Solution(object):
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if token == '+':
                    result = num1 + num2
                elif token == '*':
                    result = num1 * num2
                elif token == '/':
                    result = num1 / num2
                else:
                    result = num1 - num2

                stack.append(result)
            else:
                stack.append(token)
        return int(stack.pop())
