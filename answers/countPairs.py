# 1711. 大餐计数


class Solution:

    # twoSum改版
    def countPairs(self, deliciousness: list[int]) -> int:
        res = 0
        d_map = {}
        for i in range(len(deliciousness)):
            for j in range(0, 22):
                num = (1 << j) - deliciousness[i]
                if num in d_map:
                    res += d_map[num]
            if deliciousness[i] not in d_map:
                d_map[deliciousness[i]] = 0
            d_map[deliciousness[i]] += 1
        return res % (10**9+7)


if __name__ == '__main__':
    # print(Solution().countPairs([1,3,5,7,9]))
    # print(Solution().countPairs([1,1,1,3,3,3,7]))
    print(Solution().countPairs([149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]))
    # print(Solution().countPairs([2160,1936,3,29,27,5,2503,1593,2,0,16,0,3860,28908,6,2,15,49,6246,1946,23,105,7996,196,0,2,55,457,5,3,924,7268,16,48,4,0,12,116,2628,1468]))