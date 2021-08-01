# 31. 下一个排列


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        从后向前，找到第一个非递减的数位置i，[i+1,len]中的数都是递减的
        然后再>i的数中从后向前找到第一个比nums[i]要大的数，替换
        然后倒序[i+1,len]
        """
        i = len(nums)-2
        while i > 0 and nums[i+1] <= nums[i]:
            i -= 1
        j = len(nums)-1
        while j > i and nums[i] >= nums[j]:
            j -= 1
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        left = i
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1



if __name__ == '__main__':
    nums = [3,2,1]
    Solution().nextPermutation(nums)
