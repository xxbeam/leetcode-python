# 897. 递增顺序搜索树
import TreeNode


class Solution:

    head = TreeNode.TreeNode(0)
    temp = head

    def increasingBST(self, root: TreeNode.TreeNode) -> TreeNode.TreeNode:
        if root is None:
            return
        self.increasingBST(root.left)
        self.temp.right = TreeNode.TreeNode(root.val)
        self.temp = self.temp.right
        self.increasingBST(root.right)
        return self.head.right
