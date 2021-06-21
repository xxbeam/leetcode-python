# 483. 最小好进制

class Solution:

    def smallestGoodBase(self, n: str) -> str:
        num = int(n)

        def check(x, m):
            res = 0
            for i in range(m):
                if res > num:
                    break
                res = res * x + 1  # 秦九韶算法
            return res

        res = num  # 最坏也是num进制
        for i in range(1, 65):  # 按位数枚举，边界随便给个64位
            l, r = 2, num
            while l <= r:  # 普普通通的二分求目标值板子
                mid = (l + r) // 2
                t = check(mid, i)
                if t == num:
                    res = min(res, mid)
                    break
                if t > num:
                    r = mid - 1
                else:
                    l = mid + 1
        return str(res)


if __name__ == '__main__':
    print(Solution().smallestGoodBase("13"))
    print(Solution().smallestGoodBase("4681"))
    print(Solution().smallestGoodBase("1000000000000000000"))
