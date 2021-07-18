# 面试题 17.11. 单词距离

class Solution:
    def findClosest(self, words: list[str], word1: str, word2: str) -> int:
        """单词查找最优解"""
        # res = float("inf")
        # w1 = float("-inf")
        # w2 = float("-inf")
        # for i in range(len(words)):
        #     if words[i] == word1:
        #         w1 = i
        #         res = min(res, abs(w1-w2))
        #     if words[i] == word2:
        #         w2 = i
        #         res = min(res, abs(w1 - w2))
        # return res
        """多次查找需要hash记录"""
        word_map = {}
        for i in range(len(words)):
            if words[i] not in word_map:
                word_map[words[i]] = []
            word_map[words[i]].append(i)
        arr1 = word_map[word1]
        arr2 = word_map[word2]
        i, j = 0, 0
        res = float("inf")
        while i < len(arr1) and j < len(arr2):
            res = min(res, abs(arr1[i] - arr2[j]))
            if arr1[i] > arr2[j]:
                j += 1
            else:
                i += 1
        return res


if __name__ == '__main__':
    print(Solution().findClosest(["I","am","a","student","from","a","university","in","a","city"], "a", "student"))