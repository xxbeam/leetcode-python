# 91. 解码方法

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        return self.numDecodings1(s, len(s))

    temp_map = {}

    def numDecodings1(self, s: str, idx: int) -> int:
        if s[:idx] in self.temp_map:
            return self.temp_map.get(s[:idx])
        if 0 <= idx <= 1:
            self.temp_map[s[:idx]] = 1
            return 1
        num = 0
        if int(s[idx-1: idx]) > 0:
            num += self.numDecodings1(s, idx - 1)
        if s[idx-2] != "0" and 0 < int(s[idx-2: idx]) <= 26:
            num += self.numDecodings1(s, idx - 2)
        self.temp_map[s[:idx]] = num
        return num


if __name__ == '__main__':
    print(Solution().numDecodings("2101"))