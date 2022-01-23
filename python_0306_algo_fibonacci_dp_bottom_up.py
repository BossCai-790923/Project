memory = {0:0,
          1:1}

def fib(n):
    for i in range(n+1):
        if i <= 1:
            value = i
        else:
            value = memory[i-1] + memory[i-2]
        memory[i] = value
    return memory[n]
print(fib(34))