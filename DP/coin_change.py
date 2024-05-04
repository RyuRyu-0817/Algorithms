"""
コインの組み合わせを考える
前といた足し算のやつと同じやから詳細は省きます。
"""
def coinChange(coins, amount):
    dp = [float("INF")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for j in (coin, amount + 1):
            if dp[j - coin] != float('INF'):
                dp[j] = min(dp[j], dp[j - coin] + 1)
    return dp[amount] if dp[amount] != float("INF") else -1
coins = list(map(int, input().split()))
amount = int(input())
print(coinChange(coins, amount))
