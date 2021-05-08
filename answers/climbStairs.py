# 70. 爬楼梯

class Solution:

    def climbStairs(self, n: int) -> int:
        map = {1: 1, 2: 2}

        def climb(n):
            if n in map:
                return map.get(n)
            count = climb(n - 1) + climb(n - 2)
            map[n] = count
            return count

        return climb(n)


if __name__ == '__main__':
    print(Solution().climbStairs(3))
