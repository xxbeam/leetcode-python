# 41. 缺失的第一个正数


class Solution:

    """
    将值放到对应（值-1）的数组位置，如果完全填满则表明缺失的再length+1
    否则必然缺失正数在数组中的某一个
    """
    def firstMissingPositive(self, nums: list[int]) -> int:
        size = len(nums)
        i = 0
        while i < size:
            if 0 < nums[i] < size and nums[nums[i]-1] != nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
            else:
                i += 1
        for j in range(size):
            if nums[j] != j+1:
                return j+1
        return size+1

if __name__ == '__main__':
    print(Solution().firstMissingPositive([3,4,-1,1]))