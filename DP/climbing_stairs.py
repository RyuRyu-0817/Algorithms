"""
Dpの問題
2段登る→ 1段目までの通り数 + 0段目までの通り数
要は、n段目のぼるには、n-2段目から2段登るのとn-1段目から1段のぼる方法がある
dpで通り数を保持しておく
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]
        