# 69. x 的平方根


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l, r, e = 1, x, -1
        while l < r:
            m = (l + r) // 2
            s = m * m
            if s < x:
                e = m
                l = m + 1
            elif s > x:
                r = m
            else:
                return m
        return e


if __name__ == '__main__':
    # print(Solution().mySqrt(0))
    print(Solution().mySqrt(5))
    print(Solution().mySqrt(10))