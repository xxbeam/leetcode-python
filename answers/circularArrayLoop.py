# 457. 环形数组是否存在循环


class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return False

        def next(i):
            return (i + nums[i]) % len(nums)

        for i in range(len(nums)):
            # 双指针
            slow, fast = i, next(i)
            # 判断是否是单向边，如果一个正一个负责不符合提议，如果有为0，则表示已经访问过了
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:
                if slow == fast:
                    if slow == next(slow):
                        break
                    return True
                slow = next(slow)
                fast = next(next(fast))
            idx = i
            while nums[idx] * nums[next(idx)] > 0:
                temp = idx
                idx = next(idx)
                nums[temp] = 0
        return False