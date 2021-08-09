def unpacking_example():
    student_info = ('John', 'T0112233E', 'Oct 10th, 2007', 'Male')


    '''
    It looks like, ungroup student_info, assign its value to multiple variables.
    Actually, what happens is:
    On the left side, it is a tuple, which contains 4 values - name, ic, birthday, gender
    On the right side, it is tuple student_info 
    So this is assigning a tuple's value to the tuple on the left
    So after this, name, ic, birthday, gender will have the tuple student_info's value
    '''
    name, ic, birthday, gender = student_info
    print(name, ic, birthday, gender)

    #so this actually equals to
    (name, ic, birthday, gender) = student_info
    print(name, ic, birthday, gender)
'''
Summary
tuple unpacking means
1)Assign right tuple's value to the left tuple.
2)left tuple is composed of variables.
3)so those variable will have the right tuple's values.
This equals to: you ungroup a tuple, and assign its value to multiple variables.
'''
unpacking_example()
def unpacking_example2():
    x='jelly'
    y='bean'
    x, y =y, x
    print(x,y)# bean jelly
    # it equals to:
    (x,y)=(y,x)
    print(x,y)#jelly bean

unpacking_example2()

def unpacking_example3():
    (a,(b,(c,d)))=(4,(3,(2,1)))
    print(a,b,c,d) # 4 , 3 , 2 , 1
    # equals to:
    a, (b, (c, d)) = 4, (3, (2, 1))
    print(a, b, c, d)  # 4 , 3 , 2 , 1
unpacking_example3()
