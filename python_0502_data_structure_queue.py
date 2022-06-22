from queue import Queue


# our test code ---------------------
q = Queue()
print("enqueue/put ----------------")
q.put("eat")
q.put("sleep")
q.put("code")
print(q.qsize())

print("dequeue/get ----------------")
print(q.get())
print(q.get())
print(q.get())

print(q.empty())
print(q.qsize())