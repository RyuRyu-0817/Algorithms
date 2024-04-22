'''
基本的にunique_pathと同じで障害物があるだけ
'''
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        row = len(obstacleGrid)
        column = len(obstacleGrid[0])
        dp = [[0] * column for _ in range(row)]

        for i in range(row):
            for j in range(column):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                        continue
                    if i - 1 < 0:
                        dp[i][j] = dp[i][j - 1]
                    elif j - 1 < 0:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

                else:
                    dp[i][j] = 0

        return dp[row - 1][column] - 1
