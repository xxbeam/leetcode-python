# 461. 汉明距离


class Solution:

    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        res = 0
        for i in range(len(bin(num))-2):
            if num & 1 << i != 0:
                res += 1
        return res


if __name__ == '__main__':
    print(Solution().hammingDistance(1,4))