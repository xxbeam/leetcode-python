# 239. 滑动窗口最大值
import collections

class Solution:

    # 单调队列实现
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = collections.deque()
        result = []
        size = len(nums)
        for i in range(k):
            if i >= size:
                break
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        result.append(queue[0])
        for i in range(k, len(nums)):
            if nums[i-k] == queue[0]:
                queue.popleft()
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            result.append(queue[0])
        return result

if __name__ == '__main__':
    print(Solution().maxSlidingWindow(
[1,3,-1,-3,5,3,6,7], 3))
    # arr = [1,2,3,3,3,3,4,5]
    # arr.remove(3)
    # print(arr)