# 81. 搜索旋转排序数组 II


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        if not nums:
            return False
        if target < nums[0]:
            if target > nums[-1]:
                return False
            for i in range(len(nums)-1, -1, -1):
                if nums[i] == target:
                    return True
                if i-1 >= 0 and nums[i] < nums[i-1]:
                    return False
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    return True
                if i + 1 < len(nums) and nums[i] > nums[i + 1]:
                    return False

        return False


if __name__ == '__main__':
    print(Solution().search([5,1,3], 3))