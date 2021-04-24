# 1335. 工作计划的最低难度
import sys


class Solution:



    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        if d == 1:
            return max(jobDifficulty)
        max_num = sys.maxsize
        size = len(jobDifficulty)
        arr = [[-1 for _ in range(size)] for _ in range(d)]
        max_diff = -1
        for i in range(size-(d-1)):
            max_diff = max(jobDifficulty[i], max_diff)
            arr[0][i] = max_diff

        for i in range(1, d-1):
            for j in range(i, size-(d-1-i)):
                arr[i][j] = max_num
                max_diff = -1
                for k in range(j, i-1, -1):
                    max_diff = max(max_diff, jobDifficulty[k])
                    arr[i][j] = min(arr[i][j], arr[i - 1][k - 1] + max_diff)
        max_diff = -1
        min_num = max_num
        for i in range(size-1, d-2, -1):
            max_diff = max(max_diff, jobDifficulty[i])
            arr[d - 1][i] = arr[d-2][i-1] + max_diff
            min_num = min(min_num, arr[d - 1][i])
        return min_num


if __name__ == '__main__':
    print(Solution().minDifficulty([6,5,4,3,2,1], 2))
    print(Solution().minDifficulty([7,1,7,1,7,1], 3))