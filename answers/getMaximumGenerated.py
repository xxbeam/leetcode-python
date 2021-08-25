# 1646. 获取生成数组中的最大值

class Solution:

    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        arr = [0] * (n+1)
        arr[1] = 1
        res = 1
        for i in range(2, n+1):
            arr[i] = arr[i // 2] + i % 2 * arr[i // 2 + 1]
            res = max(res, arr[i])
        return res


if __name__ == '__main__':
    print(Solution().getMaximumGenerated(7))
    print(Solution().getMaximumGenerated(2))
    print(Solution().getMaximumGenerated(3))