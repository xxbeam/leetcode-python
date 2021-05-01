# 1011. 在 D 天内送达包裹的能力


class Solution:
    def shipWithinDays(self, weights: list[int], D: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) >> 1
            temp = 0
            day = 1
            for w in weights:
                temp += w
                if temp > mid:
                    day += 1
                    temp = w
            if day <= D:
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    print(Solution().shipWithinDays([147,73,265,305,191,152,192,293,309,292,182,157,381,287,73,162,313,366,346,47], 10))