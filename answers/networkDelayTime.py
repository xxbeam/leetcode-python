# 743. 网络延迟时间

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        net_map = {}
        for time in times:
            if time[0] not in net_map:
                net_map[time[0]] = []
            net_map[time[0]].append([time[1], time[2]])
        arr = [float("inf")] * (n+1)
        arr[k] = 0
        queue = [k]
        while queue:
            node = queue.pop(0)
            if node in net_map:
                for net in net_map[node]:
                    if arr[node] + net[1] < arr[net[0]]:
                        queue.append(net[0])
                        arr[net[0]] = arr[node] + net[1]
        res = max(arr[1:])
        if res == float("inf"):
            return -1
        return res


if __name__ == '__main__':
    print(Solution().networkDelayTime([[1,2,1],[2,3,7],[1,3,4],[2,1,2]], 3, 1))
    print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
    print(Solution().networkDelayTime([[1,2,1]], 2, 1))
    print(Solution().networkDelayTime([[1,2,1]],2, 2))