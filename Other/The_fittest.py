"""
マスにある捕食者が近傍の動物を捕食する
捕食関係をdagで表現し、トポロジカルソートする
トポロジカルソートの先頭の捕食者から、捕食を開始する。
捕食者が誰を捕食するのかを隣接リストとして、保持し、捕食者のマスに到達したら、近傍に
非捕食者がいるかを確認する。いれば、捕食

"""

from collections import deque
from pprint import pprint

h, w = map(int, input().split())
A = [input().split() for _ in range(h)]
graph = {}
into_num = {}

n = int(input())
for _ in range(n):
    p, v = input().split()
    if not graph.get(p) and not into_num.get(p):
        into_num[p] = 0
        graph[p] = []

    if not graph.get(v) and not into_num.get(v):
        into_num[v] = 0
        graph[v] = []
    

    graph[p].append(v)
    into_num[v] +=  1

q = deque([])
for key in into_num.keys():
    if into_num[key]==0:
        q.append(key)


ans = deque([])
while q:
    v = q.popleft()
    ans.append(v)
    for adj in graph[v]:
        into_num[adj] -= 1 
        if into_num[adj]==0:
            q.append(adj) 

dxy = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
while ans:
    predator = ans.popleft()
    preys = graph[predator]

    for prey in preys:
        for i in range(h):
            for j in range(w):
                if A[i][j] == predator:
                    for dx, dy in dxy:
                        neighborx, neighbory = i + dx, j + dy
                        if 0 <= neighborx < h and 0 <= neighbory < w:
                            if A[neighborx][neighbory] == prey:
                                A[neighborx][neighbory] = '-'

for row in A:
    print(*row)