'''
Q) What is a Queue?
A) Queue is like a line of people waiting to be served.
   People can only join the tail of the queue.
   People at the head of the queue get served first before he leaves the queue.
   First-In First-Out (FIFO)
1st step, you finish a high level requirement of class Queue:
class Queue:
    def __init__(self):
        pass
    def enqueue(self, item):
        pass
    def dequeue(self):
        pass
    def empty(self):
        pass
    def size(self):
        pass
'''

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

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
IMPORTANCE!! -------------------------------------
1) You can use python list to implement a Queue class.
2) dequeue() function very slow. Time complexity O(n)
--------------------------------------------------
'''