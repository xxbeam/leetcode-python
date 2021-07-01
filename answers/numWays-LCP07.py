# LCP 07. 传递信息


class Solution:
    def numWays(self, n: int, relation: list[list[int]], k: int) -> int:
        dp = [[0] * n for _ in range(k)]
        target_map = {}
        for i, j in relation:
            if i == 0:
                dp[0][j] += 1
            if j not in target_map:
                target_map[j] = []
            target_map[j].append(i)
        for i in range(1, k):
            for j in range(n):
                if j in target_map:
                    source_arr = target_map[j]
                    for source in source_arr:
                        dp[i][j] += dp[i-1][source]
        return dp[k-1][n-1]


if __name__ == '__main__':
    print(Solution().numWays(5, [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], 3))
    print(Solution().numWays(3, [[0,2],[2,1]], 2))
