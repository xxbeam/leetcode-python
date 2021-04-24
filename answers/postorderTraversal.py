# 145. 二叉树的后序遍历
import TreeNode


class Solution:

    def postorderTraversal(self, root: TreeNode.TreeNode) -> list[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

