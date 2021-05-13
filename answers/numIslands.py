# 200. 岛屿数量


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        land = 0
        col = len(grid)
        row = len(grid[0])
        vector = set()
        for i in range(col):
            for j in range(row):
                if (i, j) not in vector:
                    if grid[i][j] == '1':
                        land += 1
                        queue = [(i, j)]
                        vector.add((i, j))
                        while queue:
                            x, y = queue.pop()
                            if x + 1 < col and (x + 1, y) not in vector and grid[x + 1][y] == '1':
                                vector.add((x + 1, y))
                                queue.append((x + 1, y))
                            if y + 1 < row and (x, y + 1) not in vector and grid[x][y + 1] == '1':
                                vector.add((x, y + 1))
                                queue.append((x, y + 1))
                            if x - 1 >= 0 and (x - 1, y) not in vector and grid[x - 1][y] == '1':
                                vector.add((x - 1, y))
                                queue.append((x - 1, y))
                            if y - 1 >= 0 and (x, y - 1) not in vector and grid[x][y - 1] == '1':
                                vector.add((x, y - 1))
                                queue.append((x, y - 1))
        return land


if __name__ == '__main__':
    print(Solution().numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))
    print(Solution().numIslands([
        ["0", "1", "0"],
        ["1", "0", "1"],
        ["0", "1", "0"]
    ]))
