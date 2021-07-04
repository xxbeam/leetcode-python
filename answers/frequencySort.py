# 451. 根据字符出现频率排序


class Solution:
    def frequencySort(self, s: str) -> str:
        s_map = {}
        for i in s:
            if i not in s_map:
                s_map[i] = 0
            s_map[i] += 1
        arr = []
        for key in s_map.keys():
            temp = []
            while arr and s_map[arr[-1]] < s_map[key]:
                temp.insert(0, arr.pop())
            arr.append(key)
            arr += temp
        res = ""
        for i in arr:
            for j in range(s_map[i]):
                res += i
        return res

if __name__ == '__main__':
    print(Solution().frequencySort("raaeaedere"))
    print(Solution().frequencySort("cccaaa"))
    print(Solution().frequencySort("Aabb"))