"""
左と右の部分木の深さを求めて、その差が1よりも大きくなっているかを再帰的に確認する。
左右の部分木の差がどちらも1以下になっていれば、その木はバランスが保たれている。
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        if abs(left-right) > 1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left), self.depth(root.right))+1
        