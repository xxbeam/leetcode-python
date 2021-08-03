# 236. 二叉树的最近公共祖先

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p == q:
            return p
        node_map = {}
        queue = [root]
        p_flag = False
        q_flag = False
        while queue:
            temp = []
            for node in queue:
                if node == p:
                    p_flag = True
                if node == q:
                    q_flag = True
                if p_flag and q_flag:
                    break
                if node.left:
                    node_map[node.left] = node
                    temp.append(node.left)
                if node.right:
                    node_map[node.right] = node
                    temp.append(node.right)
            queue = temp
        visit = set()
        while q:
            visit.add(q)
            if q in node_map:
                q = node_map[q]
            else:
                q = None
        while p:
            if p in visit:
                return p
            if p in node_map:
                p = node_map[p]
            else:
                p = None
        return None