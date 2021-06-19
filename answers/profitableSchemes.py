# 879. 盈利计划


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        total_p = sum(profit)
        size = len(group)
        if minProfit > total_p:
            return 0
        dp = [[0] * (minProfit+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(size):
            for j in range(n, group[i]-1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] += dp[j-group[i]][max(k-profit[i], 0)]
        return dp[n][minProfit] % (10**9 + 7)


if __name__ == '__main__':
    print(Solution().profitableSchemes(100, 100, [18,58,88,52,54,13,50,66,83,61,100,54,60,80,1,19,78,54,67,20,57,46,12,6,14,43,64,81,30,60,48,53,86,71,51,23,71,87,95,69,11,12,41,36,69,89,91,10,98,31,67,85,16,83,83,14,14,71,33,5,40,61,22,19,34,70,50,21,91,77,4,36,16,38,56,23,68,51,71,38,63,52,14,47,25,57,95,35,58,32,1,39,48,33,89,9,1,95,90,78], [96,77,37,98,66,44,18,37,47,9,38,82,74,12,71,31,80,64,15,45,85,52,70,53,94,90,90,14,98,22,33,39,18,22,10,46,6,19,25,50,33,15,63,93,35,0,76,44,37,68,35,80,70,66,4,88,66,93,49,19,25,90,21,59,17,40,46,79,5,41,2,37,27,92,0,53,57,91,75,0,42,100,16,97,83,75,57,61,73,21,63,97,75,95,84,14,98,47,0,13]))
    print(Solution().profitableSchemes(5, 3, [2, 2], [2, 3]))
    print(Solution().profitableSchemes(10, 5, [2,3,5], [6,7,8]))