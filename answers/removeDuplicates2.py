# 80. 删除有序数组中的重复项 II

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        i, j = 0, 1
        count = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                count += 1
                if count <= 2:
                    i += 1
                    nums[i] = nums[j]
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
                count = 1
        return i + 1


if __name__ == '__main__':
    nums = [1]
    n = Solution().removeDuplicates(nums)
    print(n)
    print(nums[:n])