# 87. 扰乱字符串

class Solution:

    temp_map = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1+"-"+s2) in self.temp_map:
            return self.temp_map.get(s1+"-"+s2)
        if s1 == s2:
            self.temp_map[s1+"-"+s2] = True
            return True
        # 如果s1和s2排序后的字符串不相等，则必定不是扰乱字符串
        if sorted(s1) != sorted(s2):
            self.temp_map[s1 + "-" + s2] = False
            return False
        for i in range(1, len(s1)):
            x = s1[:i]
            y = s1[i:]
            if (self.isScramble(x, s2[:i]) and self.isScramble(y, s2[i:]))\
                    or (self.isScramble(x, s2[0-i:]) and self.isScramble(y, s2[:0-i])):
                self.temp_map[s1 + "-" + s2] = True
                return True
        self.temp_map[s1 + "-" + s2] = False
        return False

if __name__ == '__main__':
    print(Solution().isScramble("abcdefghijklmnopq", "efghijklmnopqcadb"))

