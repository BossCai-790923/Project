'''
https://dmoj.ca/problem/coci06c5p1
'''

import sys

everything_from_input = sys.stdin.read()
all_lines = everything_from_input.split('\n')
first_line = all_lines[0]

a, b, c = 1, 0, 0

for switch_type in first_line:
    if switch_type == 'A':
        a, b = b, a
    if switch_type == 'B':
        b, c = c, b
    if switch_type == 'C':
        a, c = c, a

if a == 1:
    print('1')
if b == 1:
    print('2')
if c == 1:
    print('3')