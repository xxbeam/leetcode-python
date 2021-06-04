# 525. 连续数组

class Solution:

    """
    把0换成-1，求和为0的数组
    """
    def findMaxLength(self, nums: list[int]) -> int:
        pre_sum = 0
        map = {}
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
            pre_sum += nums[i]
            if pre_sum == 0:
                res = i + 1
            if pre_sum in map:
                res = max(i - map[pre_sum], res)
            else:
                map[pre_sum] = i
        return res

if __name__ == '__main__':
    print(Solution().findMaxLength([0,0,1,0,0,0,1,1]))
    print(Solution().findMaxLength([0,1,0]))