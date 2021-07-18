# 215. 数组中的第K个最大元素


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.sort(nums, 0, len(nums)-1, len(nums) - k)

    def sort(self, nums: list[int], l: int, r:int, idx: int):
        if l >= r:
            return nums[l]
        pos = self.randomPartition(nums, l, r)
        if pos < idx:
            return self.sort(nums, pos+1, r, idx)
        elif pos > idx:
            return self.sort(nums, l, pos-1, idx)
        else:
            return nums[pos]

    def partition(self, nums: list[int], l: int, r:int):
        i, j = l, l
        while j <= r-1:
            if nums[j] < nums[r]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomPartition(self, nums: list[int], l: int, r:int):
        mid = l + (r - l) // 2
        min_num = min(nums[l], nums[r], nums[mid])
        max_num = max(nums[l], nums[r], nums[mid])
        pos = l
        if nums[mid] != min_num or nums[mid] != max_num:
            pos = mid
        elif nums[r] != min_num or nums[r] != max_num:
            pos = r
        nums[pos], nums[r] = nums[r], nums[pos]
        return self.partition(nums, l, r)


if __name__ == '__main__':
    # print(Solution().findKthLargest([3,2,1,5,6,4], 2))
    # print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
    print(Solution().findKthLargest([0,1,2], 3))