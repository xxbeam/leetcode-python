# 611. 有效三角形的个数

class Solution:

    """
     排序，枚举最大边，然后双指针
    """
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        for x in range(len(nums)-1, 1, -1):
            l = 0
            r = x - 1
            while l < r:
                if nums[l] + nums[r] > nums[x]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res


if __name__ == '__main__':
    print(Solution().triangleNumber([4,2,3,4]))
    print(Solution().triangleNumber([2,2,3,4]))