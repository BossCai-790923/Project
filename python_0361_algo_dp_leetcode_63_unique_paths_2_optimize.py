import numpy as np

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        row_count = len(obstacleGrid)
        column_count = len(obstacleGrid[0])
        dp = np.full([row_count, column_count], -1, dtype=np.int32)
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        dp[0,0] = 1

        for i in range(0, row_count):
            for j in range(0, column_count):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i,j] = 0
                else:
                    up_number = dp[i-1,j] if i > 0 else 0
                    left_number = dp[i,j-1] if j > 0 else 0
                    dp[i,j] = up_number + left_number

        return dp[row_count -1][column_count-1]
