def len_example():
    int_set={1,2,3}
    print(f'int_set size is {len(int_set)}')

def in_example():
    int_set={1,2,3}
    print(f'is 4 in the set? {4 in int_set}')
    print(f'is 1 in the set? {1 in int_set}')

def loop_example():
    for x in {1,2,3,4,5}:
        print(x)

len_example()
in_example()
loop_example()