def update_example():
    a_set={1,2,3}
    print(a_set)

    a_set.update([2,3,4])
    print(a_set)
    a_set.update([3,4,5])
    print(a_set)
    a_set.update([4,5,6])
    print(a_set)

def union_example():
    a_set = {1, 2, 3}
    print(a_set)

    a_set = a_set.union([2, 3, 4])
    print(a_set)

    a_set = a_set.union({3, 4, 5})
    print(a_set)

    a_set = a_set.union((4, 5, 6))
    print(a_set)


    # --------------------------------------
    # 1) update() is quite similar to union
    #    update() will update the original set
    #    union() will leave the original set alone
    # 2) dict also has a similar update() method
    # --------------------------------------
update_example()
union_example()
