# 263. 丑数

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n >= 5 and n % 5 == 0:
            n = n / 5
        while n >= 3 and n % 3 == 0:
            n = n / 3
        while n >= 2 and n % 2 == 0:
            n = n / 2
        return n == 1