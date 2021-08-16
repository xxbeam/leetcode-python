# 1583. 统计不开心的朋友


class Solution:
    def unhappyFriends(self, n: int, preferences: list[list[int]], pairs: list[list[int]]) -> int:
        # 统计所有的配对情况
        pair_map = {}
        for pair in pairs:
            pair_map[pair[0]] = pair[1]
            pair_map[pair[1]] = pair[0]
        # 计算所有的亲密度
        degree_map = {}
        for i in range(len(preferences)):
            degree_map[i] = {}
            for j in range(len(preferences[i])):
                degree_map[i][preferences[i][j]] = j
        res = 0
        visit = set()
        for i in range(n):
            if i in visit:
                continue
            pair = pair_map[i]
            degree = degree_map[i][pair]
            flag = False
            for j in range(degree):
                friend = preferences[i][j]
                friend_pair = pair_map[friend]
                friend_pair = degree_map[friend][friend_pair]
                if friend_pair > degree_map[friend][i]:
                    if friend not in visit:
                        res += 1
                        visit.add(friend)
                    flag = True
            if flag:
                res += 1
                visit.add(i)
        return res


if __name__ == '__main__':
    print(Solution().unhappyFriends(4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]],  [[0, 1], [2, 3]]))
    print(Solution().unhappyFriends(2,  [[1], [0]],   [[1, 0]]))
    print(Solution().unhappyFriends(4,  [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]],    [[1, 3], [0, 2]]))