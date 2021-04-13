# 783. 二叉搜索树节点最小距离
import TreeNode


class Solution:

    def minDiffInBST(self, root: TreeNode.TreeNode) -> int:
        # 二叉搜索树中序遍历出来的数据是有序的
        arr = []
        self.inOrder(root, arr)
        min_num = arr.pop() - arr[-1]
        while len(arr) > 1:
            temp = arr.pop() - arr[-1]
            if temp < min_num:
                min_num = temp
        return min_num

    def inOrder(self, root: TreeNode.TreeNode, arr):
        if root is None:
            return
        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)
