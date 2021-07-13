# 218. 天际线问题


class Solution:

    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        x_arr = []
        # 将所有横纵坐标加入数组，并排序
        for building in buildings:
            x_arr.append(building[0])
            x_arr.append(building[1])
        x_arr.sort()
        idx = 0
        queue = []
        res = []
        for x in x_arr:
            # 将所有左边缘建筑比横坐标小的建筑加入队列中，保证队列头高度是最大的
            while idx < len(buildings) and buildings[idx][0] <= x:
                if queue:
                    if queue[0][2] < buildings[idx][2]:
                        queue.insert(0, buildings[idx])
                    elif queue[-1][2] >= buildings[idx][2]:
                        queue.append(buildings[idx])
                    else:
                        for i in range(len(queue)-1, -1, -1):
                            if queue[i][2] >= buildings[idx][2]:
                                queue.insert(i+1, buildings[idx])
                                break
                else:
                    queue.append(buildings[idx])
                idx += 1
            # 比较建筑右边缘，确保当前的横坐标x是在队列头的建筑跨度内
            while queue and queue[0][1] <= x:
                queue.pop(0)
            maxh = 0
            if queue:
                maxh = queue[0][2]
            if not res or maxh != res[-1][1]:
                res.append([x, maxh])
        return res

if __name__ == '__main__':
    print(Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
    print(Solution().getSkyline([[0,2,3],[2,5,3]]))