# 面试题 10.02. 变位词组


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        key_map = {}
        for s in strs:
            new_s = "".join(sorted(s))
            if new_s not in key_map:
                key_map[new_s] = []
            key_map[new_s].append(s)
        return list(key_map.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]))