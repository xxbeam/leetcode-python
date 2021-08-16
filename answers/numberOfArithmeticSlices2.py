# 446. 等差数列划分 II - 子序列

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        res = 0
        arr = [{}] * n
        for i in range(1, n):
            len_map = {}
            for j in range(0, i):
                x = nums[i] - nums[j]
                if x not in len_map:
                    len_map[x] = 0
                if x in arr[j]:
                    len_map[x] += arr[j][x]
                    res += arr[j][x]
                len_map[x] += 1
            arr[i] = len_map
        return res

if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices([2,2,3,4]))
    print(Solution().numberOfArithmeticSlices([2,4,6,8,10]))
    print(Solution().numberOfArithmeticSlices([7,7,7,7,7]))