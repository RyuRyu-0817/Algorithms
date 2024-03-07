"""
配列を二分探索木に変換
sortedArrayToBSTでは、配列を受け取り、真ん中の値を返す。
真ん中のノードの左右を再帰的に構築し、配列の中身がなくなれば、nullを返す
"""

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums) // 2
        if not nums:
            return None
        newNode = TreeNode(nums[mid])
        newNode.left = self.sortedArrayToBST(nums[:mid])
        newNode.right = self.sortedArrayToBST(nums[mid+1:])

        return newNode
