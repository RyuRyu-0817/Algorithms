"""
n人の中から感染者をO(logn)で見つける
1. 半分にわる
2. 多いほうを選択
1.2.を繰り返し
例 n = 7
7 ⇒ 3, 4
4 ⇒ 2, 2
2 ⇒ 1, 1
終了
"""
n = int(input())
count = 0
q = 0

while n != 1:
    q = n // 2
    r = n % 2
    n = q + r
    count += 1
print(count)