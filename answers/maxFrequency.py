# 1838. 最高频元素的频数


class Solution:

    """
    前缀和
    双指针滑动窗口
    """
    def maxFrequency(self, nums: list[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        l = 0
        r = 1
        res = 1
        pre_sum = nums[0]
        while r < len(nums):
            if nums[r] * (r-l) - pre_sum <= k:
                res = max(res, r-l+1)
                pre_sum += nums[r]
                r += 1
            else:
                pre_sum -= nums[l]
                l += 1
        return res


if __name__ == '__main__':
    print(Solution().maxFrequency([1,2,4], 5))
    print(Solution().maxFrequency([1,4,8,13], 5))
    print(Solution().maxFrequency([3,9,6], 2))