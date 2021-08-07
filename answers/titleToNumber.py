# 171. Excel表列序号


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        res = 0
        for i in range(len(columnTitle)):
            res += 26 ** (n-1-i) * (ord(columnTitle[i]) - ord('A') + 1)
        return res


if __name__ == '__main__':
    print(Solution().titleToNumber("A"))
    print(Solution().titleToNumber("AB"))
    print(Solution().titleToNumber("ZY"))