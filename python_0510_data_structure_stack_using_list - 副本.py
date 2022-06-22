class Stack:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        return self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)



# our test code ---------------------
q = Stack()
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