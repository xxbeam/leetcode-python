# 518. 零钱兑换 II

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in coins:
            for j in range(i, amount+1):
                dp[j] += dp[j-i]
        return dp[amount]


if __name__ == '__main__':
    print(Solution().change(5, [1, 2, 5]))
    print(Solution().change(3, [2]))
    print(Solution().change(10, [10]))

