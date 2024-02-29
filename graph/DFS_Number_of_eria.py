def dfs(y, x):
    if y < 0 or x < 0 or y >= h or x >= w or visited[y][x] or S[y][x] == "#":
        return
    visited[y][x] = True
    dfs(y, x-1)
    dfs(y, x+1)
    dfs(y+1, x)
    dfs(y-1, x)

h, w = map(int, input().split())
S = [input() for _ in range(h)]
visited = [[False]*w for _ in range(h)]
island = 0



for i in range(h):
    for j in range(w):
        if S[i][j] == "." and not visited[i][j]:
            dfs(i, j)
            island += 1
        
print(island)
