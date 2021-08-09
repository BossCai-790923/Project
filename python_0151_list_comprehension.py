def example1():
    list1 = list(range(10))
    tuple1 = tuple(range(10))
    range1 = range(10)
    str = 'hello python!'
    # n * 2             ->  use the variable
    # for n in list 1   ->  define a variable
    new_list1 = [n * 2 for n in list1]
    print(new_list1)
    new_list2 = [n * 3 for n in tuple1]
    print(new_list2)
    new_list3 = [n + 1 for n in range1]
    print(new_list3)
    new_list4 = [ch.upper() for ch in str]
    print(new_list4)


'''
--------------------------
summary
1
--------------------------
new_list = [expression for n in list]
new_list = [expression for n in tuple]
new_list = [expression for n in range]
new_list = [expression for n in str]
'''


def example2():
    list1 = list(range(10))
    tuple1 = tuple(range(10))
    range1 = range(10)
    str = 'The rocket came back from Mars!'

    new_list1 = [n * 2 for n in list1 if n % 2 == 1]
    print(new_list1)

    new_list2 = [n * 3 for n in tuple1 if n < 5]
    print(new_list2)

    new_list3 = [n + 1 for n in range1 if 3 < n < 8]
    print(new_list3)

    new_list4 = [ch.upper() for ch in str if ch in 'aeiou']
    print(new_list4)


'''
--------------------------
summary
2
--------------------------
new_list = [expression for n in list if boolean_expression]
new_list = [expression for n in tuple if boolean_expression]
new_list = [expression for n in range if boolean_expression]
new_list = [expression for n in str if boolean_expression]
'''


def example3():
    new_list = [0] * 10
    print(new_list)

    new_list = [0 for _ in range(10)]
    print(new_list)


# example1()
# example2()
example3()

#homework###############################
print('-----------------------------------')
my_square_list = [   i ** 2        for i in range(1, 11)     ]
print(my_square_list)
print(sum(my_square_list))