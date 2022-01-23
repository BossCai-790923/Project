import numpy as np

a = np.full([4,5], -1, dtype=np.int32)
print(a)

print('2 ways to access a single value --------------------')
print(a[2][3])
print(a[2,3])

print("assign 0 to the 2nd row --------------------------")
a[1,:] = 0

# 1   means 2nd row, as it is 0 based.
# :   means head to toe, beginning to the end.

print(a)
a[2] = 3
print(a)


print("assign -1 to the 2nd column --------------------------")
a[:,1] = 4
print(a)