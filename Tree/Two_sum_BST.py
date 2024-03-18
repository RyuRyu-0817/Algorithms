# Definition for a binary tree node.
"""
BSTの任意の二つのノードを選んで和kを作れるか。
targetノードをすべてのノードで動かし、sub = k - targetをし、足される数subを木から二分探索木の特性を使って探す。
常にtopとして、根を保存しておき、同じノードの使用を避けるため足される数が同じノードになればbreakする
O(nlogn)になる
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    top = None
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.top = root
        return self.helper(root, k)

    def helper(self, root, k):
        if root is None:
            return False
        target = root 
        sub = k - target.val 
        current = self.top
        while current:
            if sub < current.val:
                current = current.left
            elif current.val < sub:
                current = current.right
            else:
                if current.val == target.val:
                    break
                else:
                    return True

        return self.helper(root.left, k) or self.helper(root.right, k)
    
        