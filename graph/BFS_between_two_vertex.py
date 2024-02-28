"""
2点間の最短経路を出力
経路の一個前のノードをprev配列で記憶
O(n)??
"""

from collections import deque

n, x, y = map(int, input().split())
graph = [[] for _ in range(n)]
prev = [-1]*n

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

visit = deque([x])

visited = [False]*n
ans = []

while visit:
    t = visit.popleft()
    visited[t-1] = True
    if y == t:
        break
    for node in graph[t-1]:
        if not visited[node-1]:
            visit.append(node)
            prev[node-1] = t

p = y
ans = []
while p != -1:
    ans.append(p)
    p = prev[p-1]

for node in ans[::-1]:
    print(node)