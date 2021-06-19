# 279. 完全平方数


class Solution:
    def numSquares(self, n: int) -> int:
        sq = int(n ** 0.5)
        if sq * sq == n:
            return 1
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1, sq+1):
            num = i * i
            for j in range(num, n+1):
                dp[j] = min(dp[j], dp[j-num]+1)
        return dp[n]

if __name__ == '__main__':
    print(Solution().numSquares(12))
    print(Solution().numSquares(13))