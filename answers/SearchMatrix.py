# 74. 搜索二维矩阵


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for l in matrix[::-1]:
            if l and target >= l[0]:
                for i in l:
                    if i == target:
                        return True
        return False