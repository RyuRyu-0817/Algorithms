# Definition for a binary tree node.
from collections import deque
from typing import Optional, List

"""
各深さごとのノードを二次元配列で出力する。
無難なBFS
キューで保存されている長さ分のループをする。(これが各深さでのノード数になる)
キューから一つずつ取り出し、左右のノードがあればキューについかしていく
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])
        ans = []
        while q:
            q_len = len(q)
            nodes = []
            for _ in range(q_len):
                target = q.popleft()
                nodes.append(target.val)
                if target.left:
                    q.append(target.left)
                if target.right:
                    q.append(target.right)
            ans.append(nodes)

        return ans  