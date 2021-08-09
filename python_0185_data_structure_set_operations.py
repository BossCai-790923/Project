set_divisible_by_2 = set(range(0, 21, 2))
set_divisible_by_3 = set(range(0, 21, 3))
set_divisible_by_5 = set(range(0, 21, 5))

print(set_divisible_by_2)
print(set_divisible_by_3)
print(set_divisible_by_5)

# Union - 并集
set_divisible_by_2_or_5 = set_divisible_by_2.union(set_divisible_by_5)
print('set divisible by 2 or 5', set_divisible_by_2_or_5)

set_divisible_by_2_or_5 = set_divisible_by_2 | set_divisible_by_5  # pipe operator
print('set divisible by 2 or 5', set_divisible_by_2_or_5)

# Intersection - 交集
set_divisible_by_2_and_5 = set_divisible_by_2.intersection(set_divisible_by_5)
print('set divisible by 2 and 5', set_divisible_by_2_and_5)

set_divisible_by_2_and_5 = set_divisible_by_2 & set_divisible_by_5  # and operator
print('set divisible by 2 and 5', set_divisible_by_2_and_5)

# Minus - 差集
set_divisible_by_2_but_not_5 = set_divisible_by_2.difference(set_divisible_by_5)
print('set divisible by 2 but not 5', set_divisible_by_2_but_not_5)

set_divisible_by_2_but_not_5 = set_divisible_by_2 - set_divisible_by_5
print('set divisible by 2 but not 5', set_divisible_by_2_but_not_5)

# Symmetric Difference - 对称差集
set_divisible_by_2_or_5_but_not_both = set_divisible_by_2.symmetric_difference(set_divisible_by_5)
print('set divisible by 2 or 5 but not both', set_divisible_by_2_or_5_but_not_both)

set_divisible_by_2_or_5_but_not_both = set_divisible_by_2 ^ set_divisible_by_5
print('set divisible by 2 or 5 but not both', set_divisible_by_2_or_5_but_not_both)

# 并集 = 交集 + 对称差集
print('Union = intersection + symmetric difference: ',
      set_divisible_by_2_or_5 == (set_divisible_by_2_and_5 | set_divisible_by_2_or_5_but_not_both))

# Union - 并集 ->  |
# Intersection - 交集 ->  &
# Minus - 差集 ->  -
# Symmetric Difference - 对称差集 ->  ^