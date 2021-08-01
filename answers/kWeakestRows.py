# 1337. 矩阵中战斗力最弱的 K 行

class Solution:

    """
    暴力法，可以使用二分查找统计各行的军人数量
    """
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        row = len(mat)
        col = len(mat[0])
        res = []
        visit = set()
        for i in range(col):
            for j in range(row):
                if j not in visit and mat[j][i] == 0:
                    res.append(j)
                    visit.add(j)
                    if len(res) == k:
                        return res
        for i in range(row):
            if i not in visit:
                res.append(i)
                if len(res) == k:
                    break
        return res


if __name__ == '__main__':
    print(Solution().kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3))
    print(Solution().kWeakestRows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 2))