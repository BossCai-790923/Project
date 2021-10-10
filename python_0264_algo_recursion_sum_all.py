def sum_non_recursion(n):
    result = 0
    for i in range(n+1):
        result += i
    return result


def sum_recursion(n):

    result=0
    # base case:

    if n <= 1:
        return n




    result+= sum_recursion(i)
    return result







# you must pass in a non-negative number, I will omit the parameter check
result = sum_non_recursion(100)
x = sum_recursion(100)

print(result)
print(x)
