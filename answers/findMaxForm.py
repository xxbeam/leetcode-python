# 474. 一和零


class Solution:

    """
    f[i][j][k] = max(f[i-1][j][k], f[i-1][j-strs[i].zero][k-strs[i].one]+1)
    i为数组长度，j为0的个数，k为1的个数
    """
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for str in strs:
            x, y = 0, 0
            for s in str:
                if s == '0':
                    x += 1
                else:
                    y += 1
            for j in range(m, x - 1, -1):
                for k in range(n, y - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - x][k - y] + 1)
        return dp[m][n]


if __name__ == '__main__':
    print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
