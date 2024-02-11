from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
easy
中順操作,答えを常に保持しておきたいため,helper関数で値を常に保持
"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversalHelper(root, [])
    def inorderTraversalHelper(self, root: Optional[TreeNode], ans) -> List[int]:
        if root == None:
            return
        self.inorderTraversalHelper(root.left, ans)
        ans.append(root.val)
        self.inorderTraversalHelper(root.right, ans)
        return ans
        