# 8. 字符串转换整数 (atoi)


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i >= len(s):
            return 0
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1
        j = i
        while j < len(s) and s[j].isdigit():
            j += 1
        if i == j:
            return 0
        num = int(s[i:j]) * sign
        if num > 2 ** 31 -1:
            num = 2 ** 31 -1
        elif num < -2 ** 31:
            num = -2 ** 31
        return num


if __name__ == '__main__':
    print(Solution().myAtoi("42"))
    print(Solution().myAtoi("   -42"))
    print(Solution().myAtoi("4193 with words"))
    print(Solution().myAtoi("words and 987"))
    print(Solution().myAtoi("-91283472332"))