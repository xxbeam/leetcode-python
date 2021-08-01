# 300. 最长递增子序列


class Solution:

    """
    二分法，维护一个单调递增list
    每次循环遍历数组，从arr中替换掉第一个比他大的数，否则添加到末尾
    这样arr虽然不是子序列，但是是最长的子序列长度
    """
    def lengthOfLIS(self, nums: list[int]) -> int:
        arr = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > arr[-1]:
                arr.append(nums[i])
            else:
                l, r = 0, len(arr)-1
                while l < r:
                    m = l + (r - l) // 2
                    if arr[m] >= nums[i]:
                        r = m
                    else:
                        l = m + 1
                arr[l] = nums[i]
        return len(arr)


if __name__ == '__main__':
    print(Solution().lengthOfLIS([0,1,0,3,2,3]))
    print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))
    print(Solution().lengthOfLIS([4,10,4,3,8,9]))
    print(Solution().lengthOfLIS([0,1,0,3,2,3]))
    print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))