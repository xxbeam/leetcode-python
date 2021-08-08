# 1137. 第 N 个泰波那契数

class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1
        else:
            x, y, z = 0, 1, 1
            for i in range(3, n+1):
                x, y, z = y, z, x+y+z
            return z