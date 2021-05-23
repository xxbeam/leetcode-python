# 1707. 与数组中元素的最大异或值


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        class TreeNode:
            def __init__(self, val, min_num):
                self.val = val
                self.left = None
                self.right = None
                self.min_num = min_num

        min_num = min(nums)
        max_num = max(nums)
        head = TreeNode(-1, min_num)
        for i in nums:
            node = head
            for j in range(len(bin(max_num))-3, -1, -1):
                x = i & (1 << j)
                if x == 0:
                    if node.left is None:
                        temp = TreeNode(0, i)
                        node.left = temp
                    node = node.left
                    node.min_num = min(node.min_num, i)
                else:
                    if node.right is None:
                        temp = TreeNode(1, i)
                        node.right = temp
                    node = node.right
                    node.min_num = min(node.min_num, i)
            node.val = i
        res = []
        for query in queries:
            num = query[0]
            target = query[1]
            if target < head.min_num:
                res.append(-1)
                continue
            node = head
            for j in range(len(bin(max_num))-3, -1, -1):
                x = num & (1 << j)
                if (x == 0 and node.right and target >= node.right.min_num) or (node.left is None):
                    node = node.right
                else:
                    node = node.left
            res.append(node.val ^ num)
        return res


if __name__ == '__main__':
    # print(Solution().maximizeXor([536870912,0,534710168,330218644,142254206],[[558240772,1000000000],[307628050,1000000000],[3319300,1000000000],[2751604,683297522],[214004,404207941]]))
    print(Solution().maximizeXor([0,1,2,3,4],[[3,1],[1,3],[5,6]]))
    # print(Solution().maximizeXor([5,2,4,6,6,3],[[12,4],[8,1],[6,3]]))
