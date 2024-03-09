"""
十字パズル崩し 
説明：
    1. 上下左右に同じ数字があれば、消すことができる。
    2. 消した部分は、下に詰めて落とす
    を繰り返し。
    マジのごり押し

.214.
1321.
33311
13214
33324
  ⇓
.....
.....
.....
1....
1....
"""
H = int(input())
matrix = [list(input()) for _ in range(H)]

while True:
    # 消す
    rms = []
    for row in range(H):
        for col in range(5):
            if matrix[row][col] != ".":
                neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
                able_neighbors = [(r, c) for r, c in neighbors if 0 <= r < H and 0 <= c < 5]
                if all(matrix[r][c] == matrix[row][col] for r, c in able_neighbors):
                    rms.append(((row, col), able_neighbors))
    if not rms: break

    for target, able_neighbors in rms:
        row, col = target
        matrix[row][col] = "."
        for r, c in able_neighbors:
            matrix[r][c] = "."

    # 落とす
    for col in range(5):
        for row in reversed(range(H)):
            if matrix[row][col] != ".":
                for i in range(row, H):
                    if i+1 < H and matrix[i+1][col] == ".":
                        matrix[i][col], matrix[i+1][col] = matrix[i+1][col], matrix[i][col]

for ans in matrix:
    print("".join(ans))