# 1482. 制作 m 束花所需的最少天数


class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def check(mid):
            count = 0
            num = 0
            for i in bloomDay:
                if i <= mid:
                    num += 1
                else:
                    count += num//k
                    num = 0
                    if count >= m:
                        return True
            count += num//k
            if count >= m:
                return True
            return False

        if m * k > len(bloomDay):
            return -1
        l, r = min(bloomDay), max(bloomDay)+1
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    print(Solution().minDays([30,49,11,66,54,22,2,57,35], 3, 3))