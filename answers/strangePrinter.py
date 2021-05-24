# 664. 奇怪的打印机


class Solution:
    def strangePrinter(self, s: str) -> int:
        size = len(s)
        dp = [[0] * size for _ in range(size)]
        for i in range(size - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = float("inf")
                    for x in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][x] + dp[x + 1][j])
        return dp[0][-1]


if __name__ == '__main__':
    print(Solution().strangePrinter("aaabbb"))
    # print(Solution().strangePrinter("aba"))
    # print(Solution().strangePrinter("tbgtgb"))
    print(Solution().strangePrinter("abcabcabc"))
