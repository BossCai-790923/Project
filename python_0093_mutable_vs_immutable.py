print('example 01 ----------------------------0')
x = 1000  # python creates a box,put 1000 in it let x points to it
print('id of x when it is 1000:', id(x))

x = 500  # python creates a box,put 500 in it let x points to it,then previous box is thrown away
print('id of x when it is 500:', id(x))

y = x  # python let pointer y points to the same box which x points to.
print('id of y after y=x:', id(y), ' so,both x and y points to the same box.')
x = 3000  # python let pointer x points to the  box which is 3000.
print('id of x when it is 3000', id(x))
print('example 02 ----------------------------0')
t = 5  # python let pointer t points to a newly created box which holds 5.
print('id of t when it is 5', id(t))
t += 2  # For value 2, python creates a box, put 2 in it.
# Python done the math.5+2=7
# box 5 and 2 will become trash,python will throw it away
print('id of t when after t +=2:', id(t))
print('example 03 ----------------------------0')
l = list()  # python allocates 4 empty slots.python let pointer 1 points to the 1st slot
l.append(1)  # python creates a box, put int 1 into it, python creates a pointer, let the pointer points to the box
# python put the pointer into the slot 1
# slot 1 means index 0.
# till now, only slot 1 has a pointer, slot 2 to slot 4 are all empty.
# len(l) is 1.
l.append(2)
l.append(3)
l.append(4)
# Now all 4 slots are occupied.4 pointers points to 4 boxes which hold int1/2/3/4
l.insert(1, 5)  # python notices there is no able slots for list l. Python will allocate another 4 empty slots.
# python will create a new pointer in slot 5, let it points to the box which slot_4 pointer points to.
# python let the slot_4 pointer points to the box which slot_3 pointer points to.
# python let the slot_3 pointer points to the box which slot_2 pointer points to.
# python let the slot_2 pointer points to the box which slot_1 pointer points to.
# python let the slot_1 pointer points to a newly-created box which contains int 5.

popped_value = l.pop()  # the last pointer is deleted, the box which it pointed is returned.
print('example 04 ----------------------------0')
r = [2, 4, 6]  # points to a list of 3 pointers who points to 4,7,and 11
s = r[:]  # python copy the list of three pointers who points to 4,7,11
print(s)  # [4,7,11]
print(s is r)  # False
print(s[0] is r[0])  # True
print(s[1] is r[1])  # True
print(s[2] is r[2])  # True
s[1] = 17  # when you let list s pointer at slot 1 point to another box, list r pointers are unchanged.
print(r)  # [4, 7, 11]     so list r value is unchanged, because s is NOT r
print(s)  # [4, 17, 11]    only list s value is changed.
