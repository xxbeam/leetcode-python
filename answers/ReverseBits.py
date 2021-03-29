# 190. 颠倒二进制位

class Solution:
    def reverseBits(self, n: int) -> int:
        return int("{:032b}".format(n)[::-1], 2)


if __name__ == '__main__':
    print(Solution().reverseBits(43261596))
