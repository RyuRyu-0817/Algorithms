# Definition for a binary tree node.
"""
BST内の数字の最小の絶対差求める
targetノードの左側で最大のノードと右側で最小のノードの差を求めて、小さかった方が最小値とする。
currentがNoneにならないように、TreeNode(1000000)にする。最小値を取る時に必ずNoneじゃない方をとるため
nこのノードに対して2logn回かかるため、O(nlogn)になるはず。
"""
from typing import Optional
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        return self.getMinimumDifferenceHelper(root, 100000)
    

    def getMinimumDifferenceHelper(self, root, minimum):
        if root is None:
            return minimum
        target = root
        current1 = target.left if target.left else TreeNode(1000000)
        current2 = target.right if target.right else TreeNode(1000000)

        while current1.right:
            current1 = current1.right

        while current2.left:
            current2 = current2.left
        abs_dif = min(abs(target.val - current1.val), abs(target.val - current2.val))
        if minimum >= abs_dif:
            minimum = abs_dif
        return min(self.getMinimumDifferenceHelper(root.left, minimum), self.getMinimumDifferenceHelper(root.right, minimum))
     