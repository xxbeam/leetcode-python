# 1723. 完成所有工作的最短时间
import collections

class Solution:

    # 二分法，原理类似
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        def check(m):
            arr = list(jobs)
            workers = [0] * k
            return plan_work(m, workers, arr)

        def plan_work(m, workers, arr):
            if not arr:
                return True
            w = arr.pop()
            for i in range(len(workers)):
                if workers[i] + w <= m:
                    workers[i] += w
                    if plan_work(m, workers, arr):
                        return True
                    workers[i] -= w

                if workers[i] == 0:
                    break
            arr.append(w)
            return False

        l, r = max(jobs), sum(jobs)
        jobs.sort()
        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l








if __name__ == '__main__':
    print(Solution().minimumTimeRequired([1,2,4,7,8], 2))

