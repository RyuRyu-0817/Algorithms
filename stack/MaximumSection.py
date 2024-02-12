"""
和をとるときに効率よくできるかが，問題(24)。
例:1 2 3 4 5 6 7
5+6+7 = 18
次の4+5+6 = 18 - 7 + 4つまり,s += deque(キュー)の一番上にある数 + popしたやつ
O(x) + O(n-x-1) = O(n)で解決
"""

from collections import deque

n, x = map(int, input().split())
a = list(map(int, input().split()))

dq = deque([])
m = -999

# O(x)
for _ in range(x):
    dq.append(a.pop())
s = sum(dq)
if s >= m:
    m = s
    ans = s, dq[-1]
popItem = dq.popleft()

# O(n-x-1)
while a:
    while len(dq) < x:
        dq.append(a.pop())
    s += dq[-1] - popItem
    if s >= m:
        m = s
        ans = s, dq[-1]
    popItem = dq.popleft()
print(*ans)

