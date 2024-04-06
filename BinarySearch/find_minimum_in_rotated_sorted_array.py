"""
ソート済みの配列を回転した配列から最小値を求める
コメントの通り。
"""
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l + r)//2

            if nums[mid] >= nums[r]: # mid+1からrまで昇順になっている可能性があるのでmid以降を探索。midが最小値になることはないから省いてl + 1
                l = mid + 1
            
            elif nums[l] >= nums[mid]: # l+1からmidまでで最小値の候補となりえるものが存在することを示す、これはmidが最小値になる可能性もあるß
                r = mid
            else:
                return nums[l]
        
        return nums[l]