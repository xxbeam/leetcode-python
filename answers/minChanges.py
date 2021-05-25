# 1787. 使所有区间的异或结果为零


class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        size = len(nums)
        # 由于0 <= nums[i] < 2**10，所以异或的最大值必定小于2**10
        n = 2 ** 10
        dp = [[float("inf")] * n for _ in range(k)]
        # 用来记录每一列的最小值
        g = [float("inf")] * k
        for i in range(k):
            # 记录在i列数字的出现次数
            num_map = {}
            # i列总共有多少个数字
            count = 0
            for j in range(i, size, k):
                num_map[nums[j]] = num_map.get(nums[j], 0) + 1
                count += 1
            if i == 0:
                for j in range(n):
                    # 第一列，替换次数为数字总次数减去当前异或值的次数
                    dp[i][j] = min(dp[i][j], count - num_map.get(j, 0))
                    g[0] = min(g[0], dp[i][j])
            else:
                for j in range(n):
                    # 如果该列全部数字需要替换
                    dp[i][j] = g[i-1] + count
                    # 只替换除x的数字
                    for cur in num_map:
                        dp[i][j] = min(dp[i][j], dp[i-1][j^cur] + count - num_map.get(cur))
                    g[i] = min(g[i], dp[i][j])
        return dp[k-1][0]


if __name__ == '__main__':
    print(Solution().minChanges([1,2,0,3,0], 1))
    print(Solution().minChanges([3,4,5,2,1,7,3,4,7], 3))
    print(Solution().minChanges([1,2,4,1,2,5,1,2,6], 3))