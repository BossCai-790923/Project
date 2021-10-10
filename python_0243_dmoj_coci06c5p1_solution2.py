'''
https://dmoj.ca/problem/coci06c5p1
'''

cups = [1, 0, 0]

swaps = input()

for i in swaps:
    if i == 'A':
        cups.insert(0, cups.pop(1))
    if i == 'B':
        cups.insert(1, cups.pop(2))
    if i == 'C':
        cups.reverse()

print(cups.index(1) + 1)