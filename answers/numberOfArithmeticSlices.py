# 413. 等差数列划分

class Solution:

    """
    动态规划
    f(n) = f(n-1) + 1,类似于子序列
    """
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)


if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices([1,2,3,8,9,10]))
    print(Solution().numberOfArithmeticSlices([1,2,3,4]))