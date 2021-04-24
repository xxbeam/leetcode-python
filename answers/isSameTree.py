# 100. 相同的树
import TreeNode


class Solution:

    def isSameTree(self, p: TreeNode.TreeNode, q: TreeNode.TreeNode) -> bool:
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        if p is None and q is None:
            return True
        if p.val != q.val or (not self.isSameTree(p.left, q.left)) or (not self.isSameTree(p.right, q.right)):
            return False
        return True


if __name__ == '__main__':
    p = TreeNode.TreeNode(10)
    p.left = TreeNode.TreeNode(5)
    p.right = TreeNode.TreeNode(15)

    q = TreeNode.TreeNode(10)
    q.left = TreeNode.TreeNode(5, left=None, right=TreeNode.TreeNode(15))
    q.right = None
    print(Solution().isSameTree(p, q))
