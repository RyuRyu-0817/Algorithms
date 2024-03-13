from typing import List
"""
パスカルのトライアングルを作る問題
一行目から始めて、行数分ループを回す
次の行のk+1番目に注目行のk番目とk+1番目の和を代入していく
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]*i for i in range(1, numRows+1)]
        for j in range(1, numRows-1):
            for k in range(j):
                rows[j+1][k+1] = rows[j][k] + rows[j][k+1]
        return rows