# 576. 出界的路径数


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove+1)]
        dp[0][startRow][startColumn] = 1
        count = 0
        for i in range(1, maxMove+1):
            for j in range(m):
                for k in range(n):
                    if dp[i-1][j][k] > 0:
                        for (x, y) in [(j-1, k), (j+1, k), (j, k-1), (j, k+1)]:
                            if 0 <= x < m and 0 <= y < n:
                                dp[i][x][y] += dp[i-1][j][k]
                            else:
                                count += dp[i-1][j][k]
        return count % ((10 ** 9) + 7)


if __name__ == '__main__':
    print(Solution().findPaths(2,2,2,0,0))
    print(Solution().findPaths(1,3,3,0,1))