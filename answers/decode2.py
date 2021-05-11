# 1734. 解码异或后的排列


class Solution:
    def decode(self, encoded: list[int]) -> list[int]:
        # 求first， 然后与1720相同逻辑
        # 1^2^3^4^...^n
        # 2^3^4^...^n = encode[1]^encode[3]^encode[5]^...
        n = len(encoded) + 1
        total = 1
        for i in range(2, n+1):
            total = total ^ i

        idx = 3
        y = encoded[1]
        while idx < len(encoded):
            y = y ^ encoded[idx]
            idx += 2

        first = total ^ y
        arr = [first]
        for i in encoded:
            arr.append(i ^ arr[-1])
        return arr


