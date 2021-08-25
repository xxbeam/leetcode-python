# 787. K 站中转内最便宜的航班


class Solution:


    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        """
            动态规划
        """
        # dp = [float("inf")] * (n+1)
        # dp[src] = 0
        # res = float("inf")
        # for i in range(k+1):
        #     temp = [float("inf")] * (n+1)
        #     for j in range(len(flights)):
        #         if dp[flights[j][0]] == float("inf"):
        #             continue
        #         temp[flights[j][1]] = min(temp[flights[j][1]], dp[flights[j][0]]+flights[j][2])
        #     dp = temp
        #     res = min(res, dp[dst])
        # if res == float("inf"):
        #     return -1
        # return res

        """
        BFS
        """
        flight_map = {}
        for i in range(len(flights)):
            if flights[i][0] not in flight_map:
                flight_map[flights[i][0]] = []
            flight_map[flights[i][0]].append(i)

        queue = [(src, 0)]
        city_price = {src:0}
        count = 0
        res = float("inf")
        while count <= k:
            temp = []
            for (x, y) in queue:
                if x in flight_map:
                    for i in flight_map[x]:
                        price = y + flights[i][2]
                        if flights[i][1] == dst:
                            res = min(res, price)
                        else:
                            if flights[i][1] not in city_price:
                                city_price[flights[i][1]] = float("inf")
                            if city_price[flights[i][1]] > price:
                                temp.append((flights[i][1], price))
                                city_price[flights[i][1]] = price
            queue = temp
            count += 1
        if res == float("inf"):
            return -1
        return res


if __name__ == '__main__':
    print(Solution().findCheapestPrice(3, [[0,1,2],[1,2,1],[2,0,10]], 1, 2, 1))
    print(Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
    print(Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))