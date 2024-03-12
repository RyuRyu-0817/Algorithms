"""
dp入門　めっちゃ嫌い
dp[i]をiグラムの重さを作るのに必要な最小のおもり数にする
j-val（jグラムになるために注目おもりvalに何グラム足せば良いかの値）が初期化から変わっていれば（１７行目）
そのおもりを使う
"""


n, x = map(int, input().split())
a = [int(input()) for i in range(n)]

dp = [100000] * (x + 1)
dp[0] = 0


for val in a:
    for j in range(x, val-1, -1):
        if dp[j-val] != 100000:
            dp[j] = min(dp[j-val]+1, dp[j])
            
print(dp[x] if dp[x] != 100000 else -1)
