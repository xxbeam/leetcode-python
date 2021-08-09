# 313. 超级丑数

class Solution:
    """
        可以用堆去优化
    """
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        if n == 1:
            return 1
        res = [1]
        arr = []
        for num in primes:
            arr.append([num, 0])
        for i in range(2, n + 1):
            num = float("inf")
            idx = 0
            for j in range(len(arr)):
                temp = arr[j][0] * res[arr[j][1]]
                while temp == res[-1]:
                    arr[j][1] += 1
                    temp = arr[j][0] * res[arr[j][1]]
                if num > temp > res[-1]:
                    idx = j
                    num = temp
            res.append(num)
            arr[idx][1] += 1
        return res[-1]


if __name__ == '__main__':
    print(Solution().nthSuperUglyNumber(15, [3, 5, 7, 11, 19, 23, 29, 41, 43, 47]))
    print(Solution().nthSuperUglyNumber(12, [2, 7, 13, 19]))
    print(Solution().nthSuperUglyNumber(1, [2, 3, 5]))
