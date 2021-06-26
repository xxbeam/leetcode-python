# 773. 滑动谜题

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        target = "123450"
        # 转成一维数组
        s = ""
        idx = 0
        for i in board:
            for j in i:
                s += str(j)
                if j == 0:
                    idx = len(s) - 1
        if target == s:
            return 0
        queue = [(s, idx, 0)]
        visit = set()
        visit.add(s)
        while queue:
            s, idx, step = queue.pop(0)
            arr = list(s)
            if idx != 0 and idx != 3:
                arr[idx] = arr[idx - 1]
                arr[idx - 1] = "0"
                cur = "".join(arr)
                if cur == target:
                    return step+1
                if cur not in visit:
                    queue.append((cur, idx - 1, step + 1))
                    visit.add(cur)
                arr[idx-1] = arr[idx]
                arr[idx] = "0"
            if idx != 2 and idx != 5:
                arr[idx] = arr[idx + 1]
                arr[idx + 1] = "0"
                cur = "".join(arr)
                if cur == target:
                    return step + 1
                if cur not in visit:
                    queue.append((cur, idx + 1, step + 1))
                    visit.add(cur)
                arr[idx + 1] = arr[idx]
                arr[idx] = "0"

            arr[idx] = arr[(idx + 3) % 6]
            arr[(idx + 3) % 6] = "0"
            cur = "".join(arr)
            if cur == target:
                return step + 1
            if cur not in visit:
                queue.append((cur, (idx + 3) % 6, step + 1))
                visit.add(cur)
        return -1


if __name__ == '__main__':
    print(Solution().slidingPuzzle([[3,2,4],[1,5,0]]))
    print(Solution().slidingPuzzle([[1,2,3],[5,4,0]]))
    print(Solution().slidingPuzzle([[4,1,2],[5,0,3]]))
