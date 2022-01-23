
class Solution:

    def uniquePath(self, m:int, n:int) -> int:

        dp = [1] * n

        # Step 2) simply loop the 2 states, fill up the dp array using the state transition formula
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]

        # Step 3) return the last value of the dp array
        return dp[-1]