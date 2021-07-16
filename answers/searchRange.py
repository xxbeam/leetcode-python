# 34. 在排序数组中查找元素的第一个和最后一个位置


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        l, r = 0, len(nums)-1
        res = []
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] != target:
            return [-1, -1]
        res.append(l)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        res.append(r)
        return res


if __name__ == '__main__':
    print(Solution().searchRange([5,7,7,8,8,10], 8))
    print(Solution().searchRange([5,7,7,8,8,10], 6))
    print(Solution().searchRange([1], 1))