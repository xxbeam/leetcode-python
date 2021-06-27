# 909. 蛇梯棋

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        # 转成一维数组
        arr = [0]
        row = 0
        for i in range(len(board)-1, -1, -1):
            if row & 1 == 0:
                for j in range(len(board[0])):
                    arr.append(board[i][j])
            else:
                for j in range(len(board[0])-1, -1, -1):
                    arr.append(board[i][j])
            row += 1
        queue = [1]
        visit = set([1])
        target = len(arr)-1
        res = 0
        while queue:
            temp = []
            for i in queue:
                for j in range(1, 7):
                    pos = i + j
                    if pos == target:
                        return res + 1
                    elif pos > target:
                        continue
                    if pos not in visit:
                        if arr[pos] == target:
                            return res + 1
                        if arr[pos] != -1:
                            temp.append(arr[pos])
                        else:
                            temp.append(pos)
                        visit.add(pos)
            queue = temp
            res += 1
        return -1


if __name__ == '__main__':
    print(Solution().snakesAndLadders([[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]))
    print(Solution().snakesAndLadders([[-1,-1,-1],[-1,9,8],[-1,8,9]]))
