'''
https://dmoj.ca/problem/16bitswonly
'''

import sys

# Step 1) read data from question

everything_from_input = sys.stdin.read()
all_lines = everything_from_input.split('\n')

for line_index in range(1, len(all_lines) - 1):
    line = all_lines[line_index]
    numbers = line.split(' ')
    no1 = int(numbers[0])
    no2 = int(numbers[1])
    no3 = int(numbers[2])

    if no1 * no2 == no3:
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")