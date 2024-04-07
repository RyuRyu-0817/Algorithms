"""
右下のマスに行くまでのpathが何個あるかを数える
注目マスは、上からくる通り数と左からくる通り数の和になる
dp[i][j] = dp[i-1][j] + dp[i][j-1]
dfsでやると指数オーダー
"""
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]
        dp = [[1]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i-1 >= 0 and j-1 >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
