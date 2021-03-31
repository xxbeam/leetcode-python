# 90. 子集 II


class Solution:

    # 是否需要排序标识符
    flag = True

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result_arr = [[]]
        if nums:
            if self.flag:
                nums.sort()
                flag = False
            for i in range(len(nums)):
                if nums.index(nums[i]) != i:
                    continue
                temp = list(nums[i+1:])
                temp_arr = self.subsetsWithDup(temp)
                for arr in temp_arr:
                    arr.insert(0, nums[i])
                    result_arr.append(arr)
        return result_arr

