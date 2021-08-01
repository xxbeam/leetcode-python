# 668. 乘法表中第k小的数


class Solution:

    """
        二分法
    """
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(mid, m, n):
            res = 0
            for i in range(1, m+1):
                res += min(n, mid // i)
            return res
        l = 1
        r = n * m
        while l < r:
            mid = l + (r - l) // 2
            ans = count(mid, m, n)
            if ans >= k:
                r = mid
            else:
                l = mid + 1
        return l

if __name__ == '__main__':
    print(Solution().findKthNumber(3,3,5))