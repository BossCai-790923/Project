def sol1():
    test_tup = (5, 20, 3, 7, 6, 8, 45, 16)
    # for i in range(len(test_tup)):
    #     if test_tup[i]==max(test_tup):
    #         x=i
    list_tup1 = list(test_tup)
    list_tup1.remove(max(list_tup1))
    test_tup1 = tuple(list_tup1)
    list_tup3 = list(test_tup)
    list_tup3.remove(min(test_tup))
    test_tup3 = tuple(list_tup3)

    fin_tup = (max(test_tup), max(test_tup1), min(test_tup), min(test_tup3))
    print(fin_tup)

def sol2():
    tuple1 = (5, 20, 3, 7, 6, 8, 45, 16)

    tuple1 = sorted(tuple1)
    smallest1, smallest2, *_, bigger2, bigger1 = tuple1
    x = (smallest1, smallest2, bigger2, bigger1)
    print(x)

# --------------------------------------------------------------

test_tup = (5, 20, 3, 7, 6, 8, 45, 16)

def enumerate_example():
    sorted_list=sorted(test_tup)
    for index,value in enumerate(sorted_list):
        print(index,value)

    print('_'*50)

# enumerate creates a list of tuples.
def enumerate_example2():
    sorted_list=sorted(test_tup)
    for item in enumerate(sorted_list):
        print(f'{item}. its type is {type(item)}')
        index,value=item
        print(index,value)

    print('_'*50)

# solution1:sorted and loop
def solution1():
    result_list=[]
    sorted_list=sorted(test_tup)
    for index,value in enumerate(sorted_list):
        if index<2 or index>len(sorted_list)-3:
            result_list.append(value)

    result_tuple=tuple(result_list)
    print(result_tuple)
    print(result_tuple)

    print('_'*50)

# solution2 sorted and slicing
def solution2():
    sorted_list=sorted(test_tup)
    result_tuple=tuple(sorted_list[:2]+sorted_list[-2:])
    print(result_tuple)

enumerate_example()
enumerate_example2()
solution1()
solution2()
sol1()
sol2()