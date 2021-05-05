# 1473. 粉刷房子 III
import sys

class Solution:
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        # m * target * n矩阵
        dp = []
        for i in range(m):
            arr1 = []
            for j in range(target + 1):
                arr1.append([sys.maxsize] * (n + 1))
            dp.append(arr1)

        if houses[0] == 0:
            for j in range(n):
                dp[0][1][j+1] = cost[0][j]
        else:
            dp[0][1][houses[0]] = 0
        for i in range(1, m):
            # 判断房子是否已经上色
            house = houses[i]
            # 当前最多街区
            max_block = min(i + 1, target)
            if house == 0:
                for j in range(1, max_block + 1):
                    for k in range(1, n+1):
                        if j == 1:
                            # 如果街区为1，那该房子必定与上一个房子颜色一致
                            dp[i][j][k] = dp[i-1][j][k] + cost[i][k-1]
                        else:
                            for y in range(1, n + 1):
                                if y == k and dp[i-1][j][y] != -1:
                                    dp[i][j][k] = min(dp[i-1][j][y], dp[i][j][k])
                                elif y != k and dp[i-1][j-1][y] != -1:
                                    dp[i][j][k] = min(dp[i-1][j-1][y], dp[i][j][k])
                            if dp[i][j][k] != sys.maxsize:
                                dp[i][j][k] += cost[i][k-1]
            else:
                for j in range(1, max_block + 1):
                    if j == 1:
                        # 如果街区为1，那该房子必定与上一个房子颜色一致
                        dp[i][j][houses[i]] = dp[i - 1][j][houses[i]]
                    else:
                        for y in range(1, n + 1):
                            if y == houses[i] and dp[i-1][j][y] != -1:
                                dp[i][j][houses[i]] = min(dp[i-1][j][y], dp[i][j][houses[i]])
                            elif y != houses[i] and dp[i-1][j-1][y] != -1:
                                dp[i][j][houses[i]] = min(dp[i-1][j-1][y], dp[i][j][houses[i]])
        cost = min(dp[m-1][target][1:])
        if cost == sys.maxsize:
            return -1
        return cost


if __name__ == '__main__':
    # print(Solution().minCost([0,0,0,0,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3))
    # print(Solution().minCost([0,2,1,2,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3))
    # print(Solution().minCost([3,1,2,3], [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], 4, 3, 3))
    print(Solution().minCost([2,3,0], [[5,2,3],[3,4,1],[1,2,1]], 3, 3, 3))
