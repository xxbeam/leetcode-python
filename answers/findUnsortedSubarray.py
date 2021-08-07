# 581. 最短无序连续子数组

class Solution:
    """
    从左到右找最大值以及比当前最大值小的位置
    从右到左找最小值以及比当前最小值大的位置
    中间段则为需要排序的数组
    """
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        max_num, right = float("-inf"), -1
        min_num, left = float("inf"), -1
        n = len(nums)
        for i in range(n):
            if max_num <= nums[i]:
                max_num = nums[i]
            else:
                right = i
            if min_num >= nums[n-i-1]:
                min_num = nums[n-i-1]
            else:
                left = n-i-1
        if right == left == -1:
            return 0
        return right-left+1

    """
    单调栈
    """
    def findUnsortedSubarray1(self, nums: list[int]) -> int:
        stack = []
        min_idx = float("inf")
        max_idx = float("-inf")
        max_num = float("-inf")
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                idx = stack.pop()
                max_num = max(max_num, nums[idx])
                min_idx = min(min_idx, idx)
                max_idx = max(max_idx, idx)
            if max_num > nums[i]:
                max_idx = i
            else:
                stack.append(i)
        if min_idx == float("inf"):
            return 0
        return max_idx - min_idx + 1


if __name__ == '__main__':
    print(Solution().findUnsortedSubarray([2, 3, 3, 2, 4]))
    print(Solution().findUnsortedSubarray([1, 2, 3, 4]))
    print(Solution().findUnsortedSubarray([1]))
