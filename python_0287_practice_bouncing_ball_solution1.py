'''
Requirement:
A ball free falls from 100m height, each time bounces to half its original height.
Calculate
1) its total travel distance when it touches the ground 10th time.
2) the height of the ball from where it touches the ground 10th time.
'''

'''
ANALYSIS:
During each bounce, total travel distance is composed of 2 parts:
1) fall-down
2) bounce-up
drop1 = 100
bounce1 = drop1 / 2
drop2 = bounce1
bounce2 = drop2 / 2
drop3 = bounce2
bounce3 = drop3 / 2
... ... 
so the loop body is always:
drop = previous bounce
bonce = drop / 2
'''

drop = 100
total_travel_distance = 0

# the last time is only drop, whole bounce, only 9 times.

for bounce_time in range(1, 10):
    bounce = drop / 2
    total_travel_distance += drop
    total_travel_distance += bounce
    print(f'Bouncing time: {bounce_time}. Fall to the ground: {drop}m. Bounce to the sky: {bounce}m. Total travel distance: {total_travel_distance}m')
    drop = bounce

print(f"Now the ball is at height: {bounce}m, it's going to touch the ground last time.")
total_travel_distance += bounce
print(f"Its total travel distance is {total_travel_distance}m")