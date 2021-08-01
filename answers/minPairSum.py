# 1877. 数组中最大数对和的最小值


class Solution:

    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        size = len(nums)
        for i in range(size // 2):
            res = max(res, nums[i] + nums[size - 1 - i])
        return res


if __name__ == '__main__':
    print(Solution().minPairSum([3,5,2,3]))
    print(Solution().minPairSum([3,5,4,2,4,6]))
