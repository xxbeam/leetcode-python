# 802. 找到最终的安全状态


class Solution:

    """
    三色标记法
    """
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        arr = [0] * len(graph)
        def dfs(i):
            flag = True
            if arr[i] == 0:
                arr[i] = 1
                for j in graph[i]:
                    if not dfs(j):
                        flag = False
                if flag:
                    arr[i] = 2
            if arr[i] == 2:
                flag = True
            else:
                flag = False
            return flag
        for i in range(len(graph)):
            dfs(i)
        res = []
        for i in range(len(arr)):
            if arr[i] == 2:
                res.append(i)
        return res

if __name__ == '__main__':
    print(Solution().eventualSafeNodes([[1,3,4,5],[],[],[],[],[2,4]]))


