# 231. 2 的幂

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(1))
    print(Solution().isPowerOfTwo(16))
    print(Solution().isPowerOfTwo(3))
    print(Solution().isPowerOfTwo(4))
    print(Solution().isPowerOfTwo(5))