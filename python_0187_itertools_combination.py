
from itertools import combinations

comb = set(combinations(range(1, 6), 3))  # pass a range to combinations function
print(comb)

comb = tuple(combinations({1,2,3}, 2)) # pass a set to combinations function
print(comb)

comb = list(combinations({1:'a', 2:'b', 3:'c'}, 2)) # pass a dict to combinations function
print(comb)

# important ---------------------------------
# the function combinations takes 2 parameters:
# param 1: any iterable - range / list / set / str / dict
# param 2: how many items you need for each combination
# ---------------------------------------


