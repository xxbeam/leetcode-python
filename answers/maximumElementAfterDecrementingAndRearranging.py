# 1846. 减小和重新排列数组后的最大元素


class Solution:

    # 贪心，排序后，arr[i]>=arr[i-1] 如果大于1 则调整到arr[i-1]+1
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1] + 1
        return arr[-1]


if __name__ == '__main__':
    print(Solution().maximumElementAfterDecrementingAndRearranging([2,2,1,2,1]))
    print(Solution().maximumElementAfterDecrementingAndRearranging([100,1,1000]))
    print(Solution().maximumElementAfterDecrementingAndRearranging([1,2,3,4,5]))