# 1449. 数位成本和为目标值的最大数字


class Solution:
    def largestNumber(self, cost: list[int], target: int) -> str:
        dp = ["0"] * (target+1)
        for i in range(len(cost)):
            if cost[i] > target:
                continue
            dp[cost[i]] = str(i+1)

        for i in range(len(cost)-1, -1, -1):
            for j in range(cost[i], target+1):
                if dp[j-cost[i]] == "0":
                    continue
                old = dp[j]
                new = dp[j - cost[i]] + str(i + 1)
                if len(new) > len(old):
                    dp[j] = new
                elif len(new) == len(old):
                    dp[j] = max(old, new)
        return dp[target]


if __name__ == '__main__':
    print(Solution().largestNumber([4,3,2,5,6,7,2,5,5], 9))
    print(Solution().largestNumber([7,6,5,5,5,6,8,7,8], 12))
    print(Solution().largestNumber([2,4,6,2,4,6,4,4,4], 5))
    print(Solution().largestNumber([6,10,15,40,40,40,40,40,40], 47))