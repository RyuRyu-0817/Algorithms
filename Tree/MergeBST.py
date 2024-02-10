"""
二時間越え，二分探索木のマージ
同時にBFSしていき,root1しかなければ,root2のコピーを返し,
root2しかなければ,root2のコピーを返す.
両方ある場合は,二つのデータを足して,それらの右左を再帰
全て終われば,rootを返す.
o(logN + logM)
"""

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def mergeBST(root1,root2):
    if root1 is None and root2 is None:
        return None

    elif root1 is None:
        newNode = root2
        return newNode

    elif root2 is None:
        newNode = root1
        return newNode


    root = BinaryTree(root1.data + root2.data)
    root.left = mergeBST(root1.left, root2.left)
    root.right = mergeBST(root1.right, root2.right)
    return root





