
from heapq import heapify, heappop
from random import randrange


def heapsort(numList):
    heapify(numList)
    return [heappop(numList) for i in range(len(numList))]


# TEST CODE ------------------

l = [randrange(100) for _ in range(10)]
print("Original list: ", l)

l = heapsort(l)
print("sorted list: ", l)