# 98. 验证二叉搜索树
import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode.TreeNode) -> bool:
        def BST(root, min_val, max_val):
            if root is None:
                return True
            if not (min_val < root.val < max_val):
                return False
            return BST(root.left, min_val, root.val) and BST(root.right, root.val, max_val)
        return BST(root, float('-inf'), float('inf'))
