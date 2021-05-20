# 692. 前K个高频单词
import collections


class Solution:

    # 统计，然后维护一个最小堆
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        def minHeap(heap, k, word, w_map):
            if heap:
                temp = []
                while heap:
                    w = heap.pop()
                    if w_map.get(w) < w_map.get(word) or (w_map.get(w) == w_map.get(word) and word < w):
                        temp.append(w)
                    else:
                        heap.append(w)
                        heap.append(word)
                        break
                if len(heap) == 0:
                    heap.append(word)
                for i in temp[::-1]:
                    heap.append(i)
            else:
                heap.append(word)
            while len(heap) > k:
                heap.pop()

        w_map = {}
        for w in words:
            if w not in w_map:
                w_map[w] = 0
            else:
                w_map[w] += 1
        res = collections.deque()
        for w in w_map.keys():
            minHeap(res, k, w, w_map)
        return list(res)


if __name__ == '__main__':
    # print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],3))
    print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))