# 671. 二叉树中第二小的节点

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        res = float("inf")
        first = root.val
        queue = [root]
        while queue:
            node = queue.pop(0)
            if first != node.val:
                res = min(res, node.val)
            if node.left:
                queue.append(node.left)
                queue.append(node.right)
        if res == float("inf"):
            return -1
        return res
