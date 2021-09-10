# 1221. 分割平衡字符串

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 0
        res = 0
        for i in range(len(s)):
            c += 1 if s[i] == 'R' else -1
            if c == 0:
                res += 1
        return res


if __name__ == '__main__':
    print(Solution().balancedStringSplit("RLRRLLRLRL"))
    print(Solution().balancedStringSplit("RLLLLRRRLR"))
    print(Solution().balancedStringSplit("LLLLRRRR"))
    print(Solution().balancedStringSplit("RLRRRLLRLL"))
