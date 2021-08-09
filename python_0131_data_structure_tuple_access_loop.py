tup1 = 10, 20, 4, 2, 6, 1, -100, 74
tup2 =  'a ', 'b', 'c', 'd', 123, True

def access_example():
    print('max(tup1):', max(tup1))
    print('min(tup1):', min(tup1))

    print('tup2[0]:', tup2[0])      #                               tup2[0]: a
    print('tup2[1:5]:', tup2[1:5])  # 1 inclusive, 5 exclusive,     tup2[1:5]: ('b', 'c', 'd', 123)
    print('tup2[1:5:2]:', tup2[1:5:2])
    print('len(tup2):', len(tup2))


def loop_example():
    for e in tup2:
        print(e, end=' ')

def sort_example():
    sorted_list = sorted(tup1)
    print(type(sorted_list))    # <class 'list'>
    print( 'sorted_list: ', sorted_list)
    sorted_list = sorted(tup1, reverse=True)
    print( 'sorted_list: ', sorted_list)

# access_example()
# loop_example()
sort_example()
