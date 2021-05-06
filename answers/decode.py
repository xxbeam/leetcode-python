# 1720. 解码异或后的数组


class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        arr = [first]
        for i in encoded:
            arr.append(i ^ arr[-1])
        return arr

if __name__ == '__main__':
    print(1^1)
    print(1 ^ 0)
    print(4 ^ 2)
    print(6 ^ 4)