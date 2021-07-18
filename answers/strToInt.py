# 剑指 Offer 67. 把字符串转换成整数

class Solution:
    def strToInt(self, str: str) -> int:
        if not str:
            return 0
        for i in range(len(str)):
            if str[i] != " ":
                str = str[i:]
                break
        sign = 1
        idx = 0
        if str[0] == "-":
            sign = -1
            idx = 1
        elif str[0] == "+":
            idx = 1
        elif not "0" <= str[0] <= "9":
            return 0
        res = 0
        max_num = 2 ** 31 - 1
        min_num = -2 ** 31
        limit = max_num // 10
        left = max_num % 10
        for i in range(idx, len(str)):
            if not "0" <= str[i] <= "9":
                break
            x = ord(str[i]) - ord("0")
            if res > limit or (res == limit and x > left):
                # 这里有个buff，虽然负数最大值末尾是8，但是x > left，那么结果只可能是-2147483648，所以可以直接返回
                return max_num if sign == 1 else min_num
            res = res * 10 + x
        return sign * res


if __name__ == '__main__':
    # print(Solution().strToInt("42"))
    # print(Solution().strToInt("   -42"))
    # print(Solution().strToInt("4193 with words"))
    # print(Solution().strToInt("words and 987"))
    # print(Solution().strToInt("-91283472332"))
    print(Solution().strToInt("-2147483649"))
    print(Solution().strToInt("-2147483648"))