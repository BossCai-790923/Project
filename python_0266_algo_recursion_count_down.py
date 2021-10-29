import time




def count_down(n):

    time.sleep(1)
    print(n)

    # base case
    if n == 0:
        return

    return count_down(n-1)


print(count_down(10))