# 剑指 Offer 37. 序列化二叉树

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if root is None:
            return ""
        queue = [root]
        res = ""
        while queue:
            temp = []
            end = True
            for node in queue:
                if node:
                    res += str(node.val)+","
                    end = False
                    temp.append(node.left)
                    temp.append(node.right)
                else:
                    res += '#'+","
            if not end:
                queue = temp
            else:
                queue = []
        return res[:-1]

    def deserialize(self, data):
        if not data:
            return None
        arr = data.split(",")
        root = TreeNode(arr[0])

        idx = 1
        queue = [root]
        while queue:
            temp = []
            for node in queue:
                if node is None:
                    continue
                left = None
                right = None
                if arr[idx] != '#':
                    left = TreeNode(int(arr[idx]))
                if arr[idx+1] != '#':
                    right = TreeNode(int(arr[idx+1]))
                idx += 2
                node.left = left
                node.right = right
                temp.append(left)
                temp.append(right)
            queue = temp
        return root


if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    root.left = node1
    node1.left = node2
    node2.left = node3
    node3.left = node4
    code = Codec()
    code.deserialize(code.serialize(root))

