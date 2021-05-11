# 104. 二叉树的最大深度
import TreeNode


class Solution:

    def maxDepth(self, root: TreeNode.TreeNode) -> int:
        def getDepth(root, depth):
            if root is None:
                return depth
            depth += 1
            return max(getDepth(root.left, depth), getDepth(root.right, depth))

        return getDepth(root, 0)


if __name__ == '__main__':
    print(Solution().maxDepth(TreeNode.TreeNode(0)))
