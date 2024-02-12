import heapq
from typing import List
"""
回答できなかった。
入力配列をヒープ化する。
配列の長さがkになるまで、最小ヒープをpopしていく
この操作により，根のノードが常にk個の中で一番小さい(k個の中でk番目に大きい)数字になる
addでは，追加されたヒープ内で一度popしてから,根のノードを取得
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.heap = k, nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)