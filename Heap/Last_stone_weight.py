"""
問題文の説明通りの実装
比較的簡単だった。
"""

from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda stone: -stone, stones))
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            
            if x == y:
                pass
            else:
                new_stone = y - x
                heapq.heappush(stones, -new_stone)
        
        return -stones[0]

