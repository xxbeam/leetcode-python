# 154. 寻找旋转排序数组中的最小值 II


class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_num = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                min_num = min(nums[left], min_num)
                left = mid + 1
            elif nums[left] > nums[mid]:
                min_num = min(nums[mid], min_num)
                right = mid - 1
            else:
                min_num = min(nums[left], min_num)
                while left <= mid:
                    if nums[left] == nums[mid]:
                        left = left + 1
                    else:
                        break
        return min_num


if __name__ == '__main__':
    print(Solution().findMin([1,3,5]))
