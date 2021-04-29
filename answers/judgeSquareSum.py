# 633. 平方数之和
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.sqrt(c))
        while l <= r:
            temp = l * l + r * r
            if temp < c:
                l += 1
            elif temp > c:
                r -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    print(Solution().judgeSquareSum(5))
    print(Solution().judgeSquareSum(3))
    print(Solution().judgeSquareSum(4))
    print(Solution().judgeSquareSum(2))