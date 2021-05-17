# 993. 二叉树的堂兄弟节点
import TreeNode

class Solution:
    def isCousins(self, root: TreeNode.TreeNode, x: int, y: int) -> bool:
        queue = [root]
        while queue:
            temp = []
            x_flag = False
            y_flag = False
            for i in queue:
                arr = []
                if i.left:
                    arr.append(i.left.val)
                    temp.append(i.left)
                if i.right:
                    arr.append(i.right.val)
                    temp.append(i.right)
                if x in arr and y in arr:
                    return False
                if x in arr:
                    x_flag = True
                if y in arr:
                    y_flag = True
                if x_flag and y_flag:
                    return True
            if x_flag or y_flag:
                return False
            queue = temp
        return False

if __name__ == '__main__':
    node = TreeNode.TreeNode(1)
    node1 = TreeNode.TreeNode(2)
    node2 = TreeNode.TreeNode(3)
    node3= TreeNode.TreeNode(4)
    node4= TreeNode.TreeNode(5)
    node.left = node1
    node.right = node2
    node1.right = node3
    node2.right = node4
    print(Solution().isCousins(node, 5,4))
    arr = [1,2,3]
    print(arr[3:])