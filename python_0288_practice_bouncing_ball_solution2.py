total_travel_distance = 0
height = 100

'''
ANALYSIS:
1) total travel distance is composed of 1st fall-down, followed by pairs of bounce-up and fall-down.
2) 1st fall-down distance is 100m
3) The following bounce-up and fall-down are of the same height, which is half of previous height.
'''

total_travel_distance += height  # 1st fall down

for _ in range(9): # followed by 9 pairs of bounce-up and fall-down
    height = height / 2 # and their height is half of previous height
    total_travel_distance += height * 2 # add both bounce-up and fall-down to the total travel distance

print(total_travel_distance)
print(height)
