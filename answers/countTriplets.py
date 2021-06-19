# 1442. 形成两个异或相等数组的三元组数目


class Solution:

    def countTriplets(self, arr: list[int]) -> int:
        if len(arr) < 2:
            return 0
        res = 0
        xor = arr[0]
        num_map = {xor: [0]}
        for j in range(1, len(arr)):
            xor = xor ^ arr[j]
            # 如果xor为0，则表明(i,j)里的数字可以拆分成两组相等的异或数
            if xor == 0:
                res += j
            # 判断是否有前缀与xor相等 比如 (0,3) == (0,9) 那么(4,9)必然为0
            if xor in num_map:
                for x in num_map.get(xor):
                    res += j - x - 1
                num_map.get(xor).append(j)
            else:
                num_map[xor] = [j]

        return res


if __name__ == '__main__':
    print(Solution().countTriplets([2, 3, 1, 6, 7]))
    print(Solution().countTriplets([1, 1, 1, 1, 1]))
    print(Solution().countTriplets([2, 3]))
    print(Solution().countTriplets([1, 3, 5, 7, 9]))
    print(Solution().countTriplets([7, 11, 12, 9, 5, 2, 7, 17, 22]))
