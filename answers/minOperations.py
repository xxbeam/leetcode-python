# 1713. 得到子序列的最少操作次数


class Solution:

    """
    将arr中的数字转换成target中的下标
    求下标的最长递增子序列 参考300题做法
    """
    def minOperations(self, target: list[int], arr: list[int]) -> int:
        num_map = {}
        for i in range(len(target)):
            num_map[target[i]] = i
        ans = [float("-inf")]
        for num in arr:
            if num not in num_map:
                continue
            idx = num_map[num]
            if ans[-1] < num_map[num]:
                ans.append(idx)
            else:
                l, r = 0, len(ans)-1
                while l < r:
                    m = l + (r - l) // 2
                    if ans[m] >= idx:
                        r = m
                    else:
                        l = m + 1
                ans[l] = idx
        return len(target) - len(ans) + 1


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    print(arr[-1::-1])

    print(Solution().minOperations([16,7,20,11,15,13,10,14,6,8], [11,14,15,7,5,5,6,10,11,6]))
    print(Solution().minOperations([5,1,3], [9,4,2,3,4]))
    print(Solution().minOperations([6,4,8,1,3,2], [4,7,6,2,3,8,6,1]))