# 645. 错误的集合

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        arr = [0] * len(nums)
        for i in nums:
            arr[i-1] += 1
        lost = -1
        repeat = -1
        for i in range(len(arr)):
            if arr[i] == 0:
                lost = i+1
            elif arr[i] > 1:
                repeat = i+1
            if lost > 0 and repeat > 0:
                break
        return [repeat, lost]


if __name__ == '__main__':
    print(Solution().findErrorNums([2,3,2]))