import heapq
test_tup = (5, 20, 3, 7, 6, 8, 45, 16)
def solution3():
    largest2 = heapq.nlargest(2, test_tup)
    smallest2 = heapq.nsmallest(2, test_tup)
    result_tup = tuple(smallest2 + largest2[::-1])
    print(result_tup)
solution3()