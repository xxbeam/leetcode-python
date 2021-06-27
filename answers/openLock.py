# 752. 打开转盘锁
from collections import deque


class Solution:

    """
    dfs
    """
    def openLock(self, deadends: list[str], target: str) -> int:

        deadendsSet = set(deadends)
        if "0000" in deadendsSet:
            return -1
        if "0000" == target:
            return 0
        hasArriveSet = set(["0000"])
        queue = deque([("0000", 0)])

        while queue:
            cur, count = queue.popleft()
            s = list(cur)
            for i in range(4):
                temp = int(s[i])
                s[i] = str((temp + 1) % 10)
                next_s = "".join(s)
                # 分别对某一位进行加一或减一操作
                if next_s not in deadendsSet and next_s not in hasArriveSet:
                    if next_s == target:
                        return count+1
                    queue.append((next_s, count+1))
                    hasArriveSet.add(next_s)
                s[i] = str((temp - 1) % 10)
                next_s = "".join(s)
                if next_s not in deadendsSet and next_s not in hasArriveSet:
                    if next_s == target:
                        return count + 1
                    queue.append((next_s, count + 1))
                    hasArriveSet.add(next_s)
                # 将该位置重置初始状态
                s[i] = str(temp)
        return -1


if __name__ == '__main__':
    print(Solution().openLock(["0201","0101","0102","1212","2002"], "0202"))