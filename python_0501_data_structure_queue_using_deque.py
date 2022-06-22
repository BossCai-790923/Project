'''
deque means: Double Ended QUEue
The most important 4 methods:
append(v)     : add value v to the right end
pop()         : delete from the right end
appendleft(v) : add value v to the left end
popleft()     : delete from the left end
'''

from collections import deque

class Queue:

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# our test code ---------------------
q = Queue()
print("enqueue/put ----------------")
q.enqueue("eat")
q.enqueue("sleep")
q.enqueue("code")
print(q.size())

print("dequeue/get ----------------")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print(q.empty())
print(q.size())



'''
IMPORTANCE!! -------------------------------------------------------
1) You can use deque to implement a Queue class.
2) dequeue() function now is very fast. Because deque is a linkedlist
--------------------------------------------------------------------
'''