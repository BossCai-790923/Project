memory = {0:0,
          1:1}
total = 0
def fib(n):
    global total
    total += 1
    if n < 2:
        return n
    if n in memory:
        return memory[n]
    memory[n] = fib(n-2) + fib(n-1)
    return memory[n]

i = 0
while True:
    print(f"{i} : {fib(i)}, it takes {total:,} method call.")
    i += 1

#
# '''
# IMPORTANT !!! ------------------------------------------
# Summary: what is dynamic programming?
# 1) subproblem + 'reuse'
# 2) recursion + memorization
# Basic steps:
# 1) take a problem.
# 2) split it into subproblems.
# 3) solve and save those subproblem. -> key steps!
# 4) rsuse the solution of subproblem. -> key steps!
# Strongly suggestion: PLEASE WATCH IT!
# MIT Computer Science Algo Lesson
# https://www.youtube.com/watch?v=OQ5jsbhAv_M&list=PLcDimPvbmfT8qAxD6JH_kmXiQwTNcoK78
# --------------------------------------------------------
# '''