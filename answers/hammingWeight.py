# 剑指 Offer 15. 二进制中1的个数

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += 1
            n = n & (n-1)
        return res

