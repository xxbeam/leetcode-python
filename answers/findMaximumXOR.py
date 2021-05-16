# 421. 数组中两个数的最大异或值


class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        class TreeNode:
            def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None

        if len(nums) < 2:
            return 0
        head = TreeNode(0)
        size = len(bin(max(nums))) - 2
        for i in nums:
            temp = head
            for j in range(1, size+1):
                if i & (1 << (size - j)):
                    if temp.right is None:
                        temp.right = TreeNode(1)
                    temp = temp.right
                else:
                    if temp.left is None:
                        temp.left = TreeNode(0)
                    temp = temp.left
            temp.val = i
        res = 0
        for i in nums:
            temp = head
            for j in range(1, size+1):
                if i & (1 << (size - j)):
                    if temp.left:
                        temp = temp.left
                    else:
                        temp = temp.right
                else:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp = temp.left
            res = max(res, i ^ temp.val)
        return res


if __name__ == '__main__':
    print(Solution().findMaximumXOR([3,10,5,25,2,8]))
    print(Solution().findMaximumXOR( [0]))
    print(Solution().findMaximumXOR([2,4]))
    print(Solution().findMaximumXOR([8,10,2]))
    print(Solution().findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))

