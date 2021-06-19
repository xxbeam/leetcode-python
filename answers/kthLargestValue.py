# 1738. 找出第 K 大的异或坐标值

class Solution:
    def kthLargestValue(self, matrix: list[list[int]], k: int) -> int:
        res = []
        dp = [0]
        for i in matrix[0]:
            xor = dp[-1] ^ i
            dp.append(xor)
            res.append(xor)
        for i in range(1, len(matrix)):
            temp = [0]
            for j in range(len(matrix[0])):
                xor = temp[-1] ^ matrix[i][j]
                temp.append(xor)
                dp[j+1] = xor ^ dp[j+1]
                res.append(dp[j+1])
        res.sort(reverse=True)
        return res[k-1]


if __name__ == '__main__':
    print(Solution().kthLargestValue([[10,9,5],[2,0,4],[1,0,9],[3,4,8]], 10))
