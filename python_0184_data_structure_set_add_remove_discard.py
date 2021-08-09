def add_example():
    k = {81, 180}
    print(k)

    k.add(54)
    print(k)

    k.add(12)
    print(k)  ##set is unordered

    k.add(180)
    print(k)  ##set don't allow duplicate values

def remove_example():
    k={81,180}
    print(k)
    k.remove(81)
    print(k)
    if 82 in k:
        k.remove(82)
    else:
        print('82 is not in set k')

def discardexample():
    k={81,180}
    print(k)
    k.discard(82)

    print(k)

add_example()
remove_example()
discardexample()