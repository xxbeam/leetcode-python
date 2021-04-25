# 368. 最大整除子集

class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if len(nums) < 2:
            return nums
        nums.sort()
        arr = [1] * len(nums)
        arr_map = {0:[nums[0]]}
        idx = 0
        max_size = 1
        for i in range(1, len(nums)):
            half = nums[i] >> 1
            for j in range(i-1, -1, -1):
                if nums[j] <= half and nums[i] % nums[j] == 0:
                    if arr[j] + 1 > arr[i]:
                        arr[i] = arr[j] + 1
                        if j in arr_map:
                            arr_map[i] = arr_map.get(j) + [nums[i]]
                        else:
                            arr_map[i] = [nums[j], nums[i]]
                    if arr[i] > max_size:
                        idx = i
                        max_size = arr[i]
        return arr_map.get(idx)


if __name__ == '__main__':
    print(Solution().largestDivisibleSubset([1,2,4,3,9]))
