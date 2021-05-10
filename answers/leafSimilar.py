# 872. 叶子相似的树
import TreeNode

class Solution:
    def leafSimilar(self, root1: TreeNode.TreeNode, root2: TreeNode.TreeNode) -> bool:
        def leaf(root, arr):
            if root is None:
                return
            leaf(root.left, arr)
            if root.left is None and root.right is None:
                arr.append(root.val)
            leaf(root.right, arr)
        arr1, arr2 = [], []
        leaf(root1, arr1)
        leaf(root2, arr2)
        return arr1 == arr2

