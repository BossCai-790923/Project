'''
You have a knapsack which can hold W kg.
You have N items. Each item has weight & value 2 attributes.
They are stored in wt array and val array.
So:
The ith item weight is wt[i]
The ith item value is val[i]
Question: What's the maximum value the knapsack can hold?
Example (1):
N = 3, W = 4; it means, you have 3 items in total, your knapsack can hold maximum 4 kg.
wt = [1, 3, 4]
val = [15, 20, 30]
Your function should return 35, it means, maximum your knapsack can hold value $35.
You can choose the 1st item and 2nd item.
Their total weight is 4 kg, their total value is $35.
'''

'''
---------------------------------------------------------------------------------
Question 1) How to define the dp function? / What's the meaning of the dp array? 
---------------------------------------------------------------------------------
*THE QUESTION ITSELF IS ALREADY THE ANSWER TO 'HOW TO DEFINE YOUR FUNCTION'. *
The question is,                                       what's the maximum value the knapsack can hold?
To parameterize the question, it becomes,              what's the maximum value the knapsack can hold when my bag can hold W kg and I can choose len(wt) item?
What is state?
State is the parameter of your dp function
State is the index of your dp array
item index -> fibonacci 
month index -> rabbit question
step index -> jumping stairs
Knapsack question has 2 states here:
1) item index -> i
2) bag weight -> j
f(i, j):
param i: means the first i items.
param j: means my bag can hold max j kg.
f(i,j) : means my bag's max possible value when my can freely put the first i items, but my bag can hold max j kg.
so our dp array:
dp= [][]
index i : means the first i items.
index j : means my bag can hold max j kg.
dp[i,j] : means my bag's max possible value when my can freely put the first i items, but my bag can hold max j kg.
So, now the question is changed to find out the value of dp[N][W]
dp[N][W] means my bag's max possible value when my bag can freely put the first N items, but my bag can hold max W kg.
---------------------------------------------------------------------
Question 2) What's the base case? / How to initialize the dp array?
---------------------------------------------------------------------
dp = np.full([N+1,W+1], -1, dtype=np.int32)
For the first 0 item, no matter how heavy the bag can hold, the value it contain is always $0. So,
dp[0,0], dp[0,1] .... dp[0,W],set their value to 0
When my bag can hold max 0 kg, no matter how many items the bag is allowed to use, the value it contains is always $0. So,
dp[0,0], dp[1,0].....dp[N,0], set their value to 0
dp[0] = 0
dp[:,0] = 0
------------------------------------------------------------------------
Question 3) What's the state transition? From THE problem to subproblem?
------------------------------------------------------------------------
dp[N][W] means my bag's max possible value when my bag can freely put the first N items, but my bag can hold max W kg.
For this last item, the Nth item, there are 2 situation.
------------------------------------------
Situation 1) wt[N] > W, meaning I can't put the Nth item into my bag
dp[N][W] = dp[N-1][W]
------------------------------------------
Situation 2) wt[N] < W, meaning I can put the Nth item into my bag
I can either put it into my bag, or I don't put it into my bag
Case 1) I don't put the Nth item into my bag
        dp[N-1][W]
Case 2) I put the Nth item into my bag
        how heavy is Nth item? wt[N]
        What's the value of this Nth item? val[N]
        So besides the Nth item, now my bag can hold max W-wt[N] kg
        my bag's max possible value is 
        dp[N-1][W-wt[N]] + val[N]

So, dp[N][W] = max(case1, case2)
    dp[N][W] = max(dp[N-1][W], dp[N-1][W-wt[N]] + val[N])
'''

import numpy as np


class Knapsack:

    def __init__(self, bag_weight, item_weight_list, item_value_list):
        self.bag_weight = bag_weight
        self.item_weight_list = item_weight_list
        self.item_value_list = item_value_list

        # Step 1) define and init dp 2 dimension array
        item_count = len(self.item_value_list)

        self.dp = np.full([item_count + 1, self.bag_weight + 1], -1, dtype=np.int32)

        self.dp[0] = 0
        self.dp[:, 0] = 0

        print(self.dp)

    def find_max_possible_bag_value(self):
        return self.f(len(self.item_value_list), self.bag_weight)

    def f(self, n, w):

        '''
        n -> the first n item
        w -> the bag can hold w kg
        '''

        # base case
        if n <= 0:
            return 0

        if w <= 0:
            return 0

        # check my memory so that I can avoid calculation
        if self.dp[n, w] != -1:
            return self.dp[n, w]

        # recursive call
        if self.item_weight_list[n - 1] > w:
            max_value = self.f(n - 1, w)

        else:
            # case 1) I don't put
            max_value_case1 = self.f(n - 1, w)
            # case 2) I put
            max_value_case2 = self.f(n - 1, w - self.item_weight_list[n - 1]) + self.item_value_list[n - 1]
            max_value = max(max_value_case1, max_value_case2)

        # update my dp array
        self.dp[n, w] = max_value

        return max_value


# test our code ------------------------------------------
bag_weight = 8
item_weight = [2, 3, 4, 5]
item_value = [3, 4, 5, 8]

solution = Knapsack(bag_weight, item_weight, item_value)
answer = solution.find_max_possible_bag_value()
print(answer)



