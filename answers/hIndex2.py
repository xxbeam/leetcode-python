# 275. H 指数 II


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        if len(citations) == 1:
            return min(citations[0], 1)
        l = 0
        r = len(citations) - 1
        h = 0
        while l <= r:
            mid = l + (r - l) // 2
            if citations[mid] >= len(citations) - mid:
                h = len(citations) - mid
                r = mid - 1
            else:
                l = mid + 1
        return h


if __name__ == '__main__':
    print(Solution().hIndex([0,1,3,5,6]))
    print(Solution().hIndex([1,2]))
    print(Solution().hIndex([2]))
    print(Solution().hIndex([1, 2, 100]))