# 377. 组合总和 Ⅳ


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # 从1开始到target分别找到每个数字可以组成的组合数
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i-nums[j]]
        return dp[target]

