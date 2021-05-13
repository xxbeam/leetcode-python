# 1269. 停在原地的方案数


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = []
        # 能走最远距离为step的一半
        size = min(arrLen, steps//2+1)
        for i in range(steps + 1):
            dp.append([0] * size)
        dp[0][0] = 1
        for i in range(1, steps+1):
            dp[i][0], dp[i][-1] = dp[i-1][0] + dp[i-1][1], dp[i-1][-1]+dp[i-1][-2]
            for j in range(1, size-1):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] + dp[i - 1][j + 1]
                if dp[i][j] == 0:
                    break
        return dp[steps][0] % (10 ** 9+7)


if __name__ == '__main__':
    print(Solution().numWays(4, 3))
