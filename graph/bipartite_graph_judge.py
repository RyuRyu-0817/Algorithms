"""
二部グラフの判定
ノードを0と1で塗っていく。注目ノードから幅優先探索で塗り分ける。
注目ノードに隣接するノード全てを注目ノードと違うノードで塗り分ける。
既に塗分けられているものは、注目ノードと同じ数字かを判定して、同じであれば、No
"""

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [0]*n
zero_or_one = [None]*n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

q = deque([1])
zero_or_one[0] = 0


while q:
    visit = q.popleft()
    visited[visit-1] = 1
    graph[visit-1].sort()

    for node in graph[visit-1]:
        if zero_or_one[visit-1] == zero_or_one[node-1]:
            print("No")
            exit()
        if not visited[node-1]:
            zero_or_one[node-1] = 0 if zero_or_one[visit-1] == 1 else 1
            q.append(node)

print("Yes")

            