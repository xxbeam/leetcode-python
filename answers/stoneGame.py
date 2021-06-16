# 877. 石子游戏

class Solution:

    """
    dp[i][j]是[i,j]的先后手差值
    dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
    """
    def stoneGame(self, piles: list[int]) -> bool:
        size = len(piles)
        dp = [[0] * size for _ in range(size)]
        for i in range(len(piles)):
            dp[i][i] = piles[i]
        for i in range(size-2, -1, -1):
            for j in range(i+1, size):
                dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
        return dp[0][size-1] > 0
