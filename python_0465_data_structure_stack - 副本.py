'''
Q) What is stack?
A) Stack is like a stack of plates.
   When you return a clean plate, you can only put on the top.
   When you take a clean plate, you can only take from the top.
   Stack is a list which you can only add value at the tail (push), take the value at the tail (pop)
   Stack is Last-In/First-Out (LIFO)
   we can use list as a stack.
   For push: we can use append(a new value)
   For pop: we can use pop()
'''

# initial
s = []

s.append("eat")
s.append("sleep")
s.append("code")

print(s)

while s:
    print('---------------------')
    last_value = s.pop()
    print(f'The last value "{last_value}" is popped out.')
    print(f'After the last value is popped out, s now becomes: {s}')

'''
In summary, what is stack?
Stack is just just. But you can only use append() and pop() these 2 methods.
'''
