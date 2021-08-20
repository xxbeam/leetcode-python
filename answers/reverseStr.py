# 541. 反转字符串 II


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s:
            return s
        s = list(s)
        i = 0
        n = len(s)
        while i < len(s):
            begin = i
            end = i + k - 1
            if end >= n:
                end = n - 1
            i = end
            while begin < end:
                s[begin], s[end] = s[end], s[begin]
                begin += 1
                end -= 1
            i += k + 1
        return "".join(s)


if __name__ == '__main__':
    print(Solution().reverseStr("abcdefg", 3))
    print(Solution().reverseStr("abcd", 2))