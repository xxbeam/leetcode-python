# 987. 二叉树的垂序遍历

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        res = []
        if not root:
            return res
        col_map = {}
        queue = [(0, root)]
        while queue:
            temp = []
            temp_col_map = {}
            for col, node in queue:
                if node.left:
                    temp.append((col-1, node.left))
                if node.right:
                    temp.append((col+1, node.right))
                if col not in temp_col_map:
                    temp_col_map[col] = []
                temp_col_map[col].append(node.val)
            for key in temp_col_map.keys():
                if key not in col_map:
                    col_map[key] = []
                temp_col_map[key].sort()
                col_map[key] += temp_col_map[key]
            queue = temp
        keys = list(col_map.keys())
        keys.sort()
        for key in keys:
            res.append(col_map[key])
        return res




