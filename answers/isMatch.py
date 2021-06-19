# 10. 正则表达式匹配

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = []
        for i in range(len(s)+1):
            dp.append([0] * (len(p)+1))
        # 标识 ‘’ 与 ‘’ 匹配，为true
        dp[0][0] = 1
        # 初始化第一行，针对所有的*做处理
        for i in range(1, len(p)+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i - 2]
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    # 当前字符匹配，结果由前缀是否匹配
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        # 可以匹配1+行，则看j-2位置是否匹配当前字符串或者上一个字符串是否可以匹配(0+次)
                        dp[i][j] = max(dp[i][j-2], dp[i-1][j])
                    else:
                        # 只能匹配0行，则看j-2位置是否匹配当前字符串
                        dp[i][j] = dp[i][j-2]
                else:
                    dp[i][j] = 0
        return dp[len(s)][len(p)] == 1


if __name__ == '__main__':
    # print(Solution().isMatch("abcd", "d*"))
    # print(Solution().isMatch("aa", "a*"))
    # print(Solution().isMatch("ab", ".*"))
    print(Solution().isMatch("aab", "c*a*b"))
    # print(Solution().isMatch("mississippi", "mis*is*ip*."))