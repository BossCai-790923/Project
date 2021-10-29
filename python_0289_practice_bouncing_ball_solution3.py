'''
ANALYSIS:
1) If we add 100m at the far left, then the total travel distance is composed of 10 pairs of bounce-up and fall-down, both are of same height.
2) The next pair of bounce-up and fall-down are half of its previous value.
3) So I can
   a) save the 10 height value to a list
   b) sum of list
   c) double the result
   d) minus the 1st 100
'''

height = 100
list_of_height = []

for bouncing_time in range(10):
    list_of_height.append(height)
    height /= 2

total_travel_distance = sum(list_of_height) * 2 - 100
print(total_travel_distance)
print(list_of_height[-1])