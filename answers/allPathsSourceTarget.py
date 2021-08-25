# 797. 所有可能的路径
import collections

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res = []
        queue = collections.deque([[0]])
        n = len(graph)
        while queue:
            arr = queue.popleft()
            for i in graph[arr[-1]]:
                temp = arr + [i]
                if i == n-1:
                    res.append(temp)
                else:
                    queue.append(temp)
        return res

if __name__ == '__main__':
    print(Solution().allPathsSourceTarget([[1,2],[3],[3],[]]))
    print(Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))