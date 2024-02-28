"""
    bfsのナンバー小さい順に訪問していく
    bfs: O(m+n), 各頂点に行われるソート: O(dlogd) d = 2m/n
    

"""

from collections import deque

n, m, x = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

visit = deque([x])
visited = [False]*n
path = []

while visit:
    t = visit.popleft()
    visited[t-1] = True
    path.append(t)

    graph[t-1].sort() # 平均的に隣接リストの長さd = 2m/nとすると、O(dlogd)
    for node in graph[t-1]:
        if not visited[node-1] and node not in visit:
            visit.append(node)

for i in path:
    print(i)
