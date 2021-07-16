# 剑指 Offer 53 - I. 在排序数组中查找数字 I


class Solution:
    """
    二分法见 34. 在排序数组中查找元素的第一个和最后一个位置
    """
    def search(self, nums: list[int], target: int) -> int:
        idx = -1
        for i in range(len(nums)):
            if nums[i] > target:
                return 0
            if nums[i] == target:
                idx = i
                break
        if idx == -1:
            return 0
        for i in range(idx+1, len(nums)):
            if nums[i] != target:
                return i - idx
        return len(nums)-idx


if __name__ == '__main__':
    print(Solution().search([5,7,7,8,8,10], 8))
    print(Solution().search([5,7,7,8,8,10], 6))