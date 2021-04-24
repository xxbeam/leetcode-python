# 102. 二叉树的层序遍历
import TreeNode


class Solution:

    def levelOrder(self, root: TreeNode.TreeNode) -> list[list[int]]:
        orders = []
        if root is None:
            return orders
        queue = [root]
        while queue:
            order = []
            temp = []
            for i in queue:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
                order.append(i.val)
            orders.append(order)
            queue = temp
        return orders

