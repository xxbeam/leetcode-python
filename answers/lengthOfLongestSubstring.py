# 3. 无重复字符的最长子串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        res = 1
        s_map = {s[0]:0}
        for i in range(1, len(s)):
            if s[i] in s_map and s_map[s[i]] >= l:
                l = s_map[s[i]] + 1
            res = max(res, i+1-l)
            s_map[s[i]] = i
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring(""))
    print(Solution().lengthOfLongestSubstring(" "))