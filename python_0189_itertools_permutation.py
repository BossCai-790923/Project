from itertools import permutations

final_result_container = set(permutations(range(1, 6), 3))
print(f"There are {len(final_result_container)} groups, they are: {final_result_container}")
