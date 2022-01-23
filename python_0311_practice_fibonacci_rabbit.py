'''
HOMEWORK:
In month 1, there is a pair of baby rabbits.
In month 4, the pair is able to breed another pair.
Assume, the rabbit never dies, calculate the total pairs of the rabbit at month 20.
'''

'''
------------
ANALYSIS
------------
--------------------------------------------------------------------------
Question 1) how to define my dp function? what's the meaning of the dp array? 
--------------------------------------------------------------------------
* THE QUESTION ITSELF IS ALREADY THE ANSWER TO 'HOW TO DEFINE YOUR DP FUNCTION' *
The question is, what is the total pairs of the rabbit at month 20.
f(n)
param n : means month n
f(n)    : means pair count of month n
so our dp array:
dp = []
index i : month i
dp[i]   : pair count for month i
--------------------------------------------------------------------------
Question 2) What's the base case? How to initialize the dp array? 
--------------------------------------------------------------------------
When n = 1, return 1
When n = 2, return 1
When n = 3, return 1
dp = [0] * 21
dp[0], dp[1], dp[2], dp[3] = 0, 1, 1, 1
--------------------------------------------------------------------------
Question 3) What's the state transition? From THE problem to subproblem?  
--------------------------------------------------------------------------
explanation:
Each month rabbit pair count (f(n)) equals to the sum of
1) last month's rabbit pair count: f(n-1)
2) this month's newly-born rabbit pair count,
   which equals to grown-up rabbit pair count of month n (as ONE grown-up pair can reproduce ONE baby pair)
   which equals to the total rabbit pair count 3 months ago: f(n-3)

f(n) = f(n-3) + f(n-1)
'''


# naive recursive
def f0(month_index):
    # base case
    if month_index <= 3:
        return 1

    # recursive call
    return f0(month_index - 3) + f0(month_index - 1)


for i in range(1, 21):
    print(f"for month: {i}, there are {f0(i)} pairs of rabbit in total")

print('----------------------------------------------------------')

dp = [0] * 21
dp[0], dp[1], dp[2], dp[3] = 0, 1, 1, 1


# dp top down
def f1(month_index):

    # base case
    if month_index <= 3:
        return 1

    if dp[month_index] != 0:
        return dp[month_index]

    # recursive call
    dp[month_index] = f1(month_index - 3) + f1(month_index - 1)
    return dp[month_index]


for i in range(1, 21):
    print(f"for month:{i}, there are{f1(i)}pairs of rabbit in total")

print('------------------------------------')

dp = [0] * 21
dp[0], dp[1], dp[2], dp[3] = 0, 1, 1, 1


def f2(month_index):  # tabulated dp

    if dp[month_index] != 0:
        return dp[month_index]

    for i in range(4, month_index + 1):
        if dp[i] == 0:
            dp[i] = dp[i-3] + dp[i-1]

    return dp[month_index]


for i in range(1, 21):
    print(f"for month: {i}, there are {f2(i)} pairs of rabbit in total")