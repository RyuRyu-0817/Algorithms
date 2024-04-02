"""
pathの存在を調べる。
unionfind木で根っこが同じだったら、ok
"""
from typing import List

class Solution:
    parent = None

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        

    def unite(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return 
        self.parent[rooty] = rootx

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.parent = [i for i in range(n)]
        for x, y in edges:
            self.unite(x, y)
        
        return self.find(source) == self.find(destination)

