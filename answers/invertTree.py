# 226. 翻转二叉树
import TreeNode


class Solution:
    def invertTree(self, root: TreeNode.TreeNode) -> TreeNode.TreeNode:
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
