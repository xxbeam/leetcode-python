# 173. 二叉搜索树迭代器
import TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode.TreeNode):
        self.arr = []
        while root:
            self.arr.append(root)
            root = root.left

    def next(self) -> int:
        node = self.arr.pop()
        res = node.val
        node = node.right
        while node:
            self.arr.append(node)
            node = node.left
        return res

    def hasNext(self) -> bool:
        if self.arr:
            return True
        else:
            return False


if __name__ == '__main__':
    print(BSTIterator(TreeNode.TreeNode()).next())