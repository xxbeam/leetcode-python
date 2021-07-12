# 930. 和相同的二元子数组

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        res = 0
        if not nums:
            return res
        arr = [0]
        sum_map = {0:1}
        for num in nums:
            arr.append(arr[-1] + num)
        for num in arr[1:]:
            left = num - goal
            if left in sum_map:
                res += sum_map[left]
            if num not in sum_map:
                sum_map[num] = 0
            sum_map[num] += 1
        return res


if __name__ == '__main__':
    print(Solution().numSubarraysWithSum([1,0,1,0,1],2))
    print(Solution().numSubarraysWithSum([0,0,0,0,0],0))