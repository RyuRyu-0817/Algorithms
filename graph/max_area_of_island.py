"""
再帰の実装わからなくなったらここ
グリッドにある島の最大面積を求める問題
各ノードに対して、上、左、右、下の方向に対して探索を行う。
戻り値が各方向の探索マスの和になり、探索方面で何個のマスがあるかが戻り値になる。
"""
from typing import List
class Solution:


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = [[False]*len(grid[0]) for i in range(len(grid))]

        def dfs(self, row, column):
            if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or visited[row][column] or grid[row][column] != 1:
                return 0
            visited[row][column] = True
            return 1 + dfs(self, row+1, column) + dfs(self, row-1, column) + dfs(self, row, column+1) + dfs(self, row, column-1)

            
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j]:
                    area = dfs(self, i, j)
                    if area >= max_area:
                        max_area = area
        return max_area