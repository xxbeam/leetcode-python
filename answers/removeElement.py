# 27. 移除元素


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return len(nums[:i])
