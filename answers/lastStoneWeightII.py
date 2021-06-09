# 1049. 最后一块石头的重量 II


class Solution:

    """
     存在最接近总重量一半的石头堆，则碎石为total - 2 * nearly_half
    """
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total = sum(stones)
        half = total//2
        dp = [0] * (half+1)
        for i in range(len(stones)):
            for j in range(half, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        return total - 2 * dp[half]


if __name__ == '__main__':
    print(Solution().lastStoneWeightII([2,7,4,1,8,1]))
    print(Solution().lastStoneWeightII([31,26,33,21,40]))
    print(Solution().lastStoneWeightII([1,2]))