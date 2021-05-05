# 740. 删除并获得点数

class Solution:
    """
    相同数的点数相加，得到不重复的数组，变成求数组中符合条件的最大点数
    """

    def deleteAndEarn(self, nums: list[int]) -> int:
        num_map = {}
        for i in nums:
            if i in num_map:
                num_map[i] = num_map.get(i) + i
            else:
                num_map[i] = i
        arr = list(num_map.keys())
        arr.sort()
        if len(arr) == 1:
            return num_map.get(arr[0])
        dp = [0] * len(arr)
        dp[0] = num_map.get(arr[0])
        if arr[0] + 1 == arr[1]:
            dp[1] = num_map.get(arr[1])
        else:
            dp[1] = dp[0] + num_map.get(arr[1])
        max_dp = 0
        for i in range(2, len(arr)):
            if arr[i - 1] + 1 == arr[i]:
                dp[i] = max(dp[i - 1], dp[max_dp] + num_map.get(arr[i]))
                if dp[i - 1] > dp[max_dp]:
                    max_dp = i - 1
            else:
                if dp[i - 1] > dp[max_dp]:
                    max_dp = i - 1
                dp[i] = dp[max_dp] + num_map.get(arr[i])
        return max(dp[max_dp], dp[-2], dp[-1])


if __name__ == '__main__':
    print(Solution().deleteAndEarn([1, 1, 1, 2, 4, 5, 5, 5, 6]))
