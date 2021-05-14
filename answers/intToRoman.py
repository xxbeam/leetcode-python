# 12. 整数转罗马数字


class Solution:
    arr = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    def intToRoman(self, num: int) -> str:
        idx = 0
        s = ""
        while True:
            if num == 0:
                break
            x, y = self.arr[idx]
            a = num // x
            if a > 0:
                s = s + y * a
            idx += 1
            num = num % x
        return s


if __name__ == '__main__':
    print(Solution().intToRoman(3))
    print(Solution().intToRoman(4))
    print(Solution().intToRoman(9))
    print(Solution().intToRoman(58))
    print(Solution().intToRoman(1994))
