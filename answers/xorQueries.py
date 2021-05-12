# 1310. 子数组异或查询


class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        result = []

        # 0 ^ i = i
        xor = [0]
        for i in arr:
            xor.append(xor[-1] ^ i)
        for query in queries:
            result.append(xor[query[1]+1] ^ xor[query[0]])
        return result


if __name__ == '__main__':
    print(Solution().xorQueries([1,3,4,8],[[0,1],[1,2],[0,3],[3,3]]))