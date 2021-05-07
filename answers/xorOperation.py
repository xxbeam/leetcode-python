# 1486. 数组异或操作


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        num = start
        for i in range(1, n):
            start = start + 2
            num = num ^ start
        return num
