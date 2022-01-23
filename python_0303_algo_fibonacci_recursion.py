total = 0


def fib(n):

    global total
    total += 1

    if n < 2:
        return n

    return fib(n-2) + fib(n-1)


i = 0

while True:
    print(f"{i} : {fib(i)}, it takes {total:,} method call.")
    i += 1



