# 374. 猜数字大小


class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        while l <= n:
            mid = (l + n) // 2
            res = guess(mid)
            if res == 1:
                l = mid + 1
            elif res == -1:
                n = mid
            else:
                return mid



def guess(num: int) -> int:
    return 1