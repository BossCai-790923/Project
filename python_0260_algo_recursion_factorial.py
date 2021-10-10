def factorial_no_recursion(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial(n):
    # base case
    if n == 1:
        return 1
    # recursive call
    return n * factorial(n - 1)

print(factorial_no_recursion(10))
print(factorial(10))

# IMPORTANCE!!! -----------------------------------
# What is recursive algorithm?
# a function calls itself to resolve the problem.
# 2 important points:
# 1) base case
# 2) recursive call
# Summary:
# 1) Recursion is convert the problem into a smaller scale sub-problem.
# For example: factorial(n) is converted to n * factorial(n-1)
# 2) And this conversion to a smaller scale sub-problem is non-stop, until we know the answer of the smallest problem.
