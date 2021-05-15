# 13. 罗马数字转整数

class Solution:
    num_map = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    def romanToInt(self, s: str) -> int:
        size = len(s)
        res = 0
        for i in range(size-1):
            num = self.num_map.get(s[i])
            num2 = self.num_map.get(s[i+1])
            if num < num2:
                res -= num
            else:
                res += num
        res += self.num_map.get(s[-1])
        return res


if __name__ == '__main__':
    print(Solution().romanToInt("III"))
    print(Solution().romanToInt("IV"))
    print(Solution().romanToInt("IX"))
    print(Solution().romanToInt("LVIII"))
    print(Solution().romanToInt("MCMXCIV"))