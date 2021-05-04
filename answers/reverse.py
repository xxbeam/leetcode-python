# 7. 整数反转
import sys

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x = int(str(x)[::-1])
            if x < 2 ** 31 - 1:
                return x
        else:
            x = -int(str(-x)[::-1])
            if x > x < -2 ** 31:
                return x
        return 0



if __name__ == '__main__':
    max_num = pow(2, 31) -1
    min_num = pow(-2, 31)
    print(max_num)
    print(min_num)
    print(sys.maxsize)