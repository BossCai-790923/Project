def func1(a, b, c, d):
    print(a, b, c, d)


list1 = [1, 2, 3, 4]

# this doesn't work - because argument count is not the same as parameter count
# func1(list1)
# TypeError: func1() missing 3 required positional arguments: 'b', 'c', and 'd'


# this works
# asterisk (*) can unpack a list
func1(*list1)  # is the same as func1(1,2,3,4)


list2 = [1, 2, 3]
# This doesn't work - because unpacking list2 gives only 3 arguments, it is not the same as parameter count.
# func1(*list2)
# TypeError: func1() missing 1 required positional argument: 'd'




# ---example 2 ------

range_args1 = [1, 20, 2]
print(list(range(*range_args1)))  # same as print(list(range(1, 20, 2)))

# SUMMARY
# IMPORTANCE !!! ---------------------------------------
# Asterisk (*) can unpack a list into individual values
# ------------------------------------------------------

'''
Explanation:
Code exection flows from 'function caller' to 'function body'.
Function Caller   ->       Function Body
*list1                a, b, c, d
*range_args1        start, stop, step
When asterik(*)appears in 'function caller argument' positions,
This equals to convert a list to multiple variables.
This is called asterik unpacking
'''




