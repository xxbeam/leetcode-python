# 152. 乘积最大子数组

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res, max_num, min_num = float("-inf"), 1, 1
        for i in nums:
            a = max_num * i
            b = min_num * i
            max_num = max(i, a, b)
            min_num = min(i, a, b)
            res = max((res, max_num))
        return res


if __name__ == '__main__':
    print(Solution().maxProduct([-2,3,-4]))
    print(Solution().maxProduct([-2,0,-1]))