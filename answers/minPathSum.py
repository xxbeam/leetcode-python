# 64. 最小路径和

class Solution:

    # 动态规划，计算走到每个格子时的最小路径
    def minPathSum(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [0] * (col+1)
        for i in range(1, col+1):
            dp[i] = dp[i-1] + grid[0][i-1]
        for i in range(1, row):
            temp = [dp[0], dp[1]+grid[i][0]]
            for j in range(1, col):
                temp.append(min(dp[j+1], temp[-1]) + grid[i][j])
            dp = temp
        return dp[-1]
