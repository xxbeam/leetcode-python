# 554. 砖墙


class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        count_map = {}
        size = len(wall)
        max_count = 0
        for i in range(size):
            l = 0
            for j in range(len(wall[i])-1):
                l = l + wall[i][j]
                if l in count_map:
                    count_map[l] = count_map.get(l) + 1
                else:
                    count_map[l] = 1
                max_count = max(max_count, count_map.get(l))
        return size - max_count



if __name__ == '__main__':
    print(Solution().leastBricks([[4,5,1],[2,1,2,5],[1,2,1,2,4]]))
