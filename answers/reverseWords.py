# 151. 翻转字符串里的单词


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        i, j = 0, 0
        while j < len(s):
            if s[j] == " ":
                if i == j:
                    i += 1
                    j += 1
                else:
                    arr.append(s[i:j])
                    j += 1
                    i = j
            else:
                j += 1
        if i < len(s):
            arr.append(s[i:])
        reverse_s = ""
        for i in arr[::-1]:
            reverse_s += i + " "
        return reverse_s[:-1]


if __name__ == '__main__':
    print(Solution().reverseWords(" asdasd df f"))