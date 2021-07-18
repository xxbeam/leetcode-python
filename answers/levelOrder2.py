# 剑指 Offer 32 - III. 从上到下打印二叉树 III
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        arr= []
        arr.sort()