"""
グラフの連結成分を求める問題
n個のノードを順に走査していく。訪問済みのノードは飛ばす。
各ノードのdfsが終わるたびにcountを＋していく

"""
import sys

sys.setrecursionlimit(10 ** 6)


def dfs(now):
    visited[now-1] = True
    graph[now-1].sort()
    for node in graph[now-1]:
        if not visited[node-1]:
            dfs(node)


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False]*n

count = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

for i in range(1, n+1):
    if visited[i-1]:
        continue
    dfs(i)
    count += 1

print(count)
            
