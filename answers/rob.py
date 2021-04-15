# 213. 打家劫舍 II


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        # 偷第一家
        arr1 = [0] * len(nums)
        arr1[0] = nums[0]
        arr1[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            arr1[i] = max(arr1[i-1], arr1[i-2] + nums[i])

        arr1[-1] = arr1[-2]

        # 偷第最后一家
        arr2 = [0] * len(nums)
        arr2[0] = 0
        arr2[1] = nums[1]
        for i in range(2, len(nums)):
            arr2[i] = max(arr2[i - 1], arr2[i - 2] + nums[i])
        max_num = max(arr1)
        max_num = max(max(arr2),max_num)
        return max_num


if __name__ == '__main__':
    print(Solution().rob([4,1,2]))
