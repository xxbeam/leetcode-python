# 528. 按权重随机选择
import random


class Solution:

    def __init__(self, w: list[int]):
        self.w = w
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.count = 0
        self.index = 0

    def pickIndex(self) -> int:
        x = random.randint(1, self.w[-1])
        l = 0
        r = len(self.w) - 1
        while l < r:
            m = l + (r - l) // 2
            if self.w[m] > x:
                r = m
            elif self.w[m] < x:
                l = m + 1
            else:
                return m
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
