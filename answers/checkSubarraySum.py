# 523. 连续的子数组和


class Solution:

    """
    计算总和，如果i、j的总和余数相同，则(i,j)组成的数组符合条件
    """
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        pre_sum = nums[0]
        map = {pre_sum % k: 0}
        for i in range(1, len(nums)):
            pre_sum += nums[i]
            left = pre_sum % k
            if left == 0:
                return True
            elif left in map and i - map[left] > 1:
                return True
            else:
                map[left] = i
        return False

if __name__ == '__main__':
    print(Solution().checkSubarraySum([1,0], 2))
    print(Solution().checkSubarraySum([0], 2))
    print(Solution().checkSubarraySum([23,2,6,4,7], 6))
    print(Solution().checkSubarraySum([23,2,6,4,7], 13))
