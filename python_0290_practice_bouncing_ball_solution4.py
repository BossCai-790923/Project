def find_last_fall_down_height(initial_height, bouncing_times):

    # base condition
    if bouncing_times == 1:
        return initial_height

    # recursive call
    # the last fall down height of the ball, for situation: initial height = 100m, bounce times = 10
    # is the same as
    # the last fall down height of the ball, for situation: initial height = 50m, bounce times = 9
    # is the same as
    # the last fall down height of the ball, for situation: initial height = 25m, bounce times = 8
    return find_last_fall_down_height(initial_height / 2, bouncing_times - 1)


def find_bounce_total_travel_distance(initial_height, bouncing_times):

    # base condition
    if bouncing_times == 1:
        return initial_height

    '''
    ANALYSIS:
    Total travel distance for situation: initial height = 100m, bounce times = 10
    is the same as, the sum of:
    1) 1st time fall down from initial height
    2) 1st time bounce back to half initial height
    3) total travel distance for situation: initial height = 50m, bounce times = 9
    '''
    # recursive call
    return initial_height + initial_height / 2 + find_bounce_total_travel_distance(initial_height / 2, bouncing_times - 1)



print(find_last_fall_down_height(100, 10))
print(find_bounce_total_travel_distance(100, 10))
#
# for i in range(1, 11):
#     last_height = find_last_fall_down_height(100, i)
#     total_distance = find_bounce_total_travel_distance(100, i)
#     print(f"bouncing times: {i}, last height : {last_height}m. Total travel distance: {total_distance}m")
