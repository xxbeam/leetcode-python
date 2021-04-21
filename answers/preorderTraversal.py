# 144. 二叉树的前序遍历
import TreeNode


class Solution:

    def preorderTraversal(self, root: TreeNode.TreeNode) -> list[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
