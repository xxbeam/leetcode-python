# 121. 买卖股票的最佳时机


class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        min_profit = 0
        max_profit = 0
        for i in range(len(prices)):
            profit = prices[i] - prices[0]
            if profit < min_profit:
                min_profit = profit
            elif profit - min_profit > max_profit:
                max_profit = profit - min_profit
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
