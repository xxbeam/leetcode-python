# 112. 路径总和
import TreeNode

class Solution:
    def hasPathSum(self, root: TreeNode.TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        targetSum = targetSum - root.val
        if root.left is None and root.right is None:
            if targetSum == 0:
                return True
            else:
                return False
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
