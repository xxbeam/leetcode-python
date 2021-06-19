# 494. 目标和

class Solution:


    """
        (max_num - n_target) - n_target = target
        转换成是否加上nums[i] 使 total  = n_target
    """
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        max_num = sum(nums)
        target = abs(target)
        if target > max_num or (max_num-target) % 2 != 0:
            return 0
        n_target = (max_num - target) // 2
        dp = [0] * (n_target+1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(n_target, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[n_target]

if __name__ == '__main__':
    print(Solution().findTargetSumWays([1,1,1,1,1], 3))
    print(Solution().findTargetSumWays([1], 2))
