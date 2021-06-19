# 1074. 元素和为目标值的子矩阵数量

class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = 0

        """
        先确定上下边界， 计算边界内从0到n的矩阵，
        如果矩阵等于target，res+1, 
        如果矩阵-target在前面已经生成的矩阵中，则res+符合矩阵的个数
        """
        for i in range(m):
            temp = [0] * n
            for j in range(i, m):
                map = {}
                total = 0
                for x in range(n):
                    temp[x] += matrix[j][x]
                    total += temp[x]
                    if total == target:
                        res += 1
                    if total - target in map:
                        res += map[total-target]
                    map[total] = map.setdefault(total, 0) + 1
        return res

if __name__ == '__main__':
    print(Solution().numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 1))
    print(Solution().numSubmatrixSumTarget([[1,-1],[-1,1]], 0))
    print(Solution().numSubmatrixSumTarget([[904]], 0))
