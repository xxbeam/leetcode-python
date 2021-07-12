# 274. H 指数

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_quote = max(citations)
        arr = [0] * (max_quote+1)
        total = len(citations)
        for citation in citations:
            arr[citation] += 1
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
        for i in range(len(arr)-1, 0, -1):
            if total - arr[i-1] >= i:
                return i
        return 0
        '''
        if len(citations) == 1:
            return min(citations[0], 1)
        citations.sort(reverse = True)
        for i in range(len(citations)):
            if i >= citations[i]:
                return i
        return min(min(citations), len(citations))
        '''