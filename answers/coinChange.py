# 322. 零钱兑换


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if not coins:
            return -1
        dp = [0] * (amount+1)
        for i in range(1, amount+1):
            dp[i] = min(float("inf") if i-j < 0 else (dp[i - j] + 1) for j in coins)
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]

if __name__ == '__main__':
    print(Solution().coinChange([186,419,83,408], 6249))
    # print(Solution().coinChange([1, 2, 5], 11))
    # print(Solution().coinChange([2], 3))
    # print(Solution().coinChange([1], 0))
    # print(Solution().coinChange([1], 1))
    # print(Solution().coinChange([1], 2))

