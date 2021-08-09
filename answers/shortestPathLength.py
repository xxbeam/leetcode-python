# 847. 访问所有节点的最短路径
import collections

class Solution:

    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        q = collections.deque((i, 1 << i, 0) for i in range(n))
        seen = {(i, 1 << i) for i in range(n)}
        ans = 0

        while q:
            u, mask, dist = q.popleft()
            if mask == (1 << n) - 1:
                ans = dist
                break
            # 搜索相邻的节点
            for v in graph[u]:
                # 将 mask 的第 v 位置为 1
                mask_v = mask | (1 << v)
                if (v, mask_v) not in seen:
                    q.append((v, mask_v, dist + 1))
                    seen.add((v, mask_v))

        return ans


if __name__ == '__main__':
    print(Solution().shortestPathLength([[1,2,3],[0],[0],[0]]))
    print(Solution().shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))