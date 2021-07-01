# 815. 公交路线
import collections


class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        bus_map = {}
        for i in range(len(routes)):
            for s in routes[i]:
                if s not in bus_map:
                    bus_map[s] = []
                bus_map[s].append(i)
        if source == target:
            return 0
        queue = collections.deque([(source, 0)])
        visit_bus = set()
        while queue:
            cur, step = queue.popleft()
            if cur in bus_map:
                for i in bus_map[cur]:
                    if i not in visit_bus:
                        for s in routes[i]:
                            if s == target:
                                return step+1
                            queue.append((s, step+1))
                        visit_bus.add(i)
        return -1


if __name__ == '__main__':
    print(Solution().numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))
    print(Solution().numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))
