'''
leetcode 225
https://leetcode.com/problems/implement-stack-using-queues/
'''


from queue import Queue

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        if self.q1.empty():
            self.q2.put(x)
        else:
            self.q1.put(x)


    def pop(self) -> int:
        if not self.q1.empty(): # if q1 is not empty, then move all value except the last one from q1 to q2
            while self.q1.qsize() > 1:
                self.q2.put(self.q1.get())
            return self.q1.get() # so that I can return the last pushed value ( this is pop of stack!)

        if not self.q2.empty(): # if q2 is not empty, then move all value except the last one from q2 to q1
            while self.q2.qsize() > 1:
                self.q1.put(self.q2.get())
            return self.q2.get() # so that I can return the last pushed value ( this is pop of stack!)

        return None


    def top(self) -> int:
        v = self.pop()
        if v != None:
            self.push(v)
        return v


    def empty(self) -> bool:
        return self.q1.empty() and self.q2.empty()

    def size(self) -> int:
        if self.q1.empty():
            return self.q2.qsize()
        else:
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