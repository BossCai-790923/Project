
from queue import Queue

class MyStack:

    def __init__(self):
        self.q1 = Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)
        for _ in range(self.q1.qsize() - 1):
            self.q1.put(self.q1.get())

    def pop(self) -> int:
        return self.q1.get()

    def top(self) -> int:
        v = self.pop()
        if v != None:
            self.push(v)
        return v


    def empty(self) -> bool:
        return self.q1.empty()

    def size(self) -> int:
        return self.q1.qsize()


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