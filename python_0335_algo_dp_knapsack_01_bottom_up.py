
import numpy as np

class Knapsack:

    def __init__(self, bag_weight, item_weight_list, item_value_list):
        self.bag_weight = bag_weight
        self.item_weight_list = item_weight_list
        self.item_value_list = item_value_list

        # Step 1) define and init dp 2 dimension array
        item_count = len(self.item_value_list)

        self.dp = np.full([item_count+1, self.bag_weight+1], -1, dtype=np.int32)

        self.dp[0] = 0
        self.dp[:,0] = 0

        print(self.dp)

    def find_max_possible_bag_value(self):

        for w in range(1, self.bag_weight + 1):
            for n in range(1, len(self.item_value_list) + 1):

                if self.item_weight_list[n - 1] > w:
                    self.dp[n, w] = self.dp[n - 1, w]
                else:
                    self.dp[n, w] = max(self.dp[n - 1, w],
                                        self.dp[n - 1, w - self.item_weight_list[n - 1]] + self.item_value_list[n - 1])

                print('----------------------------------------')
                print(self.dp)


        return self.dp[len(self.item_value_list), self.bag_weight]


# test our code ------------------------------------------
bag_weight = 8
item_weight = [2,3,4,5]
item_value = [3,4,5,8]

solution = Knapsack(bag_weight, item_weight, item_value)
answer = solution.find_max_possible_bag_value()
print(answer)


