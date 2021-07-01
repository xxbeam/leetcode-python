# 168. Excel表列名称

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            i = columnNumber % 26
            res = chr(ord('A') + i) + res
            columnNumber = columnNumber // 26
        return res


if __name__ == '__main__':
    print(Solution().convertToTitle(2147483647))
    print(Solution().convertToTitle(52))
    print(Solution().convertToTitle(701))