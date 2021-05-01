# 938. 二叉搜索树的范围和
import TreeNode


class Solution:
    def rangeSumBST(self, root: TreeNode.TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0
        if high < root.val:
            return self.rangeSumBST(root.left, low, high)
        if low <= root.val <= high:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        if low > root.val:
            return self.rangeSumBST(root.right, low, high)



if __name__ == '__main__':
    node = TreeNode.TreeNode(3)
    node.left = TreeNode.TreeNode(1)
    node.right = TreeNode.TreeNode(4)
    print(Solution().rangeSumBST(node, 2, 4))