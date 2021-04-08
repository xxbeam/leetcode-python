# 153. 寻找旋转排序数组中的最小值


class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        min_num = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                min_num = min(nums[left], min_num)
                left = mid + 1
            else:
                min_num = min(nums[mid], min_num)
                right = mid - 1
        return min_num
