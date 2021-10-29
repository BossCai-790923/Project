list_fibonacci=[0]
def fibonacci(int1,int2):
    list_fibonacci.append(int1+int2)

    if len(list_fibonacci)==100:
        return list_fibonacci
    else:
        return fibonacci(list_fibonacci[-1],list_fibonacci[-2])

print(fibonacci(0,1))
list_fibonacci=[0]
for i in range(100):
    list_fibonacci.
