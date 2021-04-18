# 26. 删除有序数组中的重复项

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        size = len(nums)
        if size <= 1:
            return size
        i, j = 0, 1
        while j < size:
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return len(nums[:i+1])


if __name__ == '__main__':
    nums = [1,1,2]
    print(Solution().removeDuplicates(nums))
    print(nums)