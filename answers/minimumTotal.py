# 120. 三角形最小路径和


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [0] * len(triangle[-1])
        for i in range(len(triangle[-1])):
            dp[i] = triangle[-1][i]
        for i in range(len(triangle)-2, -1, -1):
            temp = []
            for j in range(len(triangle[i])):
                temp.append(min(dp[j], dp[j+1]) + triangle[i][j])
            dp = temp
        return dp[0]


if __name__ == '__main__':
    print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(Solution().minimumTotal([[-10]]))