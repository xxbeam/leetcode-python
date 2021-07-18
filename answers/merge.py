# 56. 合并区间

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = []
        i = 0
        while i < len(intervals):
            begin = intervals[i][0]
            end = intervals[i][1]
            i = i+1
            while i < len(intervals) and intervals[i][0] <= end:
                end = max(end, intervals[i][1])
                i += 1
            res.append([begin, end])
        return res

if __name__ == '__main__':
    print(Solution().merge([[2,6],[8,10],[15,18],[1,3]]))
    print(Solution().merge([[1,4],[4,5]]))