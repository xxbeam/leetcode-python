# 278. 第一个错误的版本


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        if isBadVersion(l):
            return l
        else:
            return l-1


def isBadVersion(version):
    return True