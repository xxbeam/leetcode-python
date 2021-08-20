# 345. 反转字符串中的元音字母


class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(ch: str) -> bool:
            return ch in "aeiouAEIOU"
        s = list(s)
        n = len(s)
        i, j = 0, n-1
        while i < j:
            while i < n and not isVowel(s[i]):
                i += 1
            while j >= 0 and not isVowel(s[j]):
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)


if __name__ == '__main__':
    print(Solution().reverseVowels("hello"))
    print(Solution().reverseVowels("leetcode"))