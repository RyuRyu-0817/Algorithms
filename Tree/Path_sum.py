"""
helper関数を用意して、常に和を再帰で保持するようにする。
注目のノードの両方のノードがない場合(つまり葉)のみ、期待する和になっているかを確認してそれを再起的に行う。
左右のノードのどちらかが、期待する和になっていればtrue
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        return self.helper(root, targetSum, 0)
    
    def helper(self, root, targetSum, sum):
        if root is None: return False
        if root.left is None and root.right is None:
            return sum+root.val == targetSum
        return self.helper(root.left, targetSum, sum+root.val) or self.helper(root.right, targetSum, sum+root.val)
        