# 863. 二叉树中所有距离为 K 的结点


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    """ 找到每个节点的父节点，然后从target开始dfs，向下和向上同时搜索"""
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        if k == 0:
            return [target.val]
        # 每个节点的父节点
        node_map = {}
        queue = [root]
        while queue:
            node = queue.pop()
            if node.left:
                node_map[node.left] = node
                queue.append(node.left)
            if node.right:
                node_map[node.right] = node
                queue.append(node.right)
        queue = [target]
        step = 0
        visit = set()
        visit.add(target)
        res = []
        while queue:
            temp = []
            if step == k:
                for node in queue:
                    res.append(node.val)
            else:
                for node in queue:
                    if node.left and node.left not in visit:
                        temp.append(node.left)
                    if node.right and node.right not in visit:
                        temp.append(node.right)
                    if node in node_map and node_map[node] not in visit:
                        temp.append(node_map[node])
                    visit.add(node)
                step += 1
            queue = temp
        return res


if __name__ == '__main__':
    node = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node.left = node1
    node1.right = node2
    node2.right = node3
    node3.right = node4
    print(Solution().distanceK(node, node3, 0))