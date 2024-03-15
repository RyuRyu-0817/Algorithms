"""
二分探索で挿入位置を求める問題
単に二分探索をしていって、leftとrightの間の要素が一つしかなくなったら
その最後の要素がtargetよりも大きいかどうかで求める
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while right != left:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        
        return left if nums[left] >= target else left+1
