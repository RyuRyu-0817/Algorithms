"""
裁判官を探せ x -> y （これはxがyを信頼していることを表す）
裁判官の条件
①誰も信頼していない つまり出次数が0
②皆から信頼されている つまり入次数がn-1
隣接行列で表現し、列がすべて1のものを裁判官の候補として、配列に入れる
その候補列に対して、出次数がないことを見る
"""
from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = [[0]*(n+1) for _ in range(n+1)]
        candidates = []
        for x, y in trust:
            adj[x][y] = 1
        for i in range(1, n+1):
            is_candidate = True
            for j in range(1,n+1):
                if adj[j][i] == 0 and i != j:
                    is_candidate = False
                    break
            if is_candidate:
                candidates.append(i)
        for candidate in candidates:   
            is_judge = True              
            for j in range(1, n+1):
                if adj[candidate][j] == 1:
                    is_judge = False
                    break
            if is_judge:
                return candidate
            
        return -1
                