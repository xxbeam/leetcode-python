# 1743. 从相邻元素对还原数组


class Solution:

    """
    hash保存所有的数字对应的左右节点，然后找出长度=1的，表示是左右端点
    """
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        num_map = {}
        for adjacentPair in adjacentPairs:
            if adjacentPair[0] not in num_map:
                num_map[adjacentPair[0]] = []
            if adjacentPair[1] not in num_map:
                num_map[adjacentPair[1]] = []
            num_map[adjacentPair[0]].append(adjacentPair[1])
            num_map[adjacentPair[1]].append(adjacentPair[0])
        first_arr = []
        for key in num_map.keys():
            if len(num_map[key]) == 1:
                first_arr.append(key)
            if len(first_arr) == 2:
                break
        res = [0] * (len(adjacentPairs) + 1)
        l, r = 0, len(res)-1
        begin = first_arr[0]
        end = first_arr[1]
        vector = set(first_arr)
        while l <= r:
            res[l] = begin
            res[r] = end
            vector.add(begin)
            vector.add(end)
            for i in num_map[begin]:
                if i not in vector:
                    begin = i
                    break
            for i in num_map[end]:
                if i not in vector:
                    end = i
                    break
            l += 1
            r -= 1
        return res


if __name__ == '__main__':
    print(Solution().restoreArray([[2,1],[3,4],[3,2]]))
    print(Solution().restoreArray([[4,-2],[1,4],[-3,1]]))
    print(Solution().restoreArray([[100000,-100000]]))