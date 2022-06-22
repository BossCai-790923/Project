'''
leetcode 225
https://leetcode.com/problems/implement-stack-using-queues/
'''

'''
q=Queue()
q.put('x')  -> enqueue
q.get() -> dequeue
q.empty()
q.qsize()
-----------
Analysis
-----------
'''


from queue import Queue

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        return self.push(x)


    def pop(self) -> int:
        pass


    def top(self) -> int:
        pass


    def empty(self) -> bool:
        pass


    def size(self) -> int:
        pass


# our test code ---------------------
q = MyStack()
print("push ----------------")
q.push("eat")
q.push("sleep")
q.push("code")
print(q.size()) # 3

print("pop ----------------")
print(q.pop()) # code
print(q.top()) # sleep
print(q.pop()) # sleep
print(q.pop()) # eat

print(q.empty())
print(q.size())

from collections import deque


class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = None

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.queue == None:
            self.queue = deque([x])
        else:
            self.queue = deque([x, self.queue])

    # @return nothing
    def pop(self):
        if self.queue != None:
            self.queue.popleft()
            try:
                self.queue = self.queue.popleft()
            except:
                self.queue = None

    # @return an integer
    def top(self):
        return self.queue[0]

    # @return an boolean
    def empty(self):
        return self.queue == None