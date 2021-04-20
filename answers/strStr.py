# 28. 实现 strStr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(haystack) < len(needle):
            return -1
        i, j = 0, 0
        while j < len(needle) and i + j < len(haystack):
            if needle[j] == haystack[i + j]:
                if j == len(needle) - 1:
                    return i
                else:
                    j += 1
            else:
                i += 1
                j = 0
        return -1

    #BM算法
    def strStr1(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(haystack) < len(needle):
            return -1
        # 坏字符
        arr = [-1] * 26
        # 好后缀
        suffix = [-1] * len(needle)
        prefix = [False] * len(needle)
        n_len = len(needle) - 1
        for i in range(len(needle)):
            arr[ord(needle[i]) - ord("a")] = i
            if i < len(needle) - 1:
                j = i
                k = 0
                while j >= 0 and needle[j] == needle[n_len - k]:
                    j -= 1
                    k += 1
                    suffix[k] = j + 1
                if j == -1:
                    prefix[k] = True
        i = 0
        while i <= len(haystack) - len(needle):
            j = len(needle)-1
            for idx in range(len(needle)-1, -1, -1):
                if haystack[i+j] == needle[j]:
                    j -= 1
                else:
                    break
            if j < 0:
                return i
            # 坏前缀
            x = (j - arr[ord(haystack[i+j]) - ord("a")])
            # 好后缀
            y = 0
            if j < len(needle) - 1:
                y = len(needle)
                k = len(needle) - 1 - j
                if suffix[k] != -1:
                    y = j - suffix[k] + 1
                else:
                    for idx in range(j+1, len(needle)):
                        if prefix[len(needle) - idx]:
                            y = idx
            i = i + max(x, y)
        return -1



if __name__ == '__main__':
    haystack = "babbbbbabb"
    needle = "bbab"
    print(Solution().strStr1(haystack, needle))
