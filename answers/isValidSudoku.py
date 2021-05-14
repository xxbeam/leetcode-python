# 36. 有效的数独

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        num_map = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in num_map:
                    arr = num_map.get(board[i][j])
                    for (r, c, b_r, b_c) in arr:
                        if r == i or c == j or (b_r == i // 3 and b_c == j // 3):
                            return False
                    arr.append((i, j, i // 3, j // 3))
                    num_map[board[i][j]] = arr
                else:
                    num_map[board[i][j]] = [(i, j, i // 3, j // 3)]
        return True


if __name__ == '__main__':
    print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
