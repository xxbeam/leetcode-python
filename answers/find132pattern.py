# 456. 132 模式

class Solution:

    """
    单调递减栈(2)， k(3)为比栈中元素小的元素中最大值
    向前遍历数组，如果有一个元素i(1)比K要小
    则符合132模式
    """
    def find132pattern(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        k = float("-inf")
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < k:
                return True
            while stack and stack[-1] < nums[i]:
                k = max(k, stack.pop())
            stack.append(nums[i])
        return False


if __name__ == '__main__':
    print(Solution().find132pattern([3,5,0,3,4]))
    print(Solution().find132pattern([3,1,4,2]))
    print(Solution().find132pattern([-1,3,2,0]))
