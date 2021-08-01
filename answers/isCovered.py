# 1893. 检查是否区域内所有整数都被覆盖


class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        arr = [0] * 51
        for range_arr in ranges:
            for i in range(range_arr[0], range_arr[1]+1):
                arr[i] = 1
        for i in range(left, right+1):
            if arr[i] != 1:
                return False
        return True
