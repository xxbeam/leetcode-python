# 剑指 Offer 38. 字符串的排列

class Solution:
    def permutation(self, s: str) -> list[str]:
        res = []
        def nextPermutation(arr):
            i = len(arr)-2
            while i>=0 and arr[i] >= arr[i+1]:
                i -= 1
            if i < 0:
                return
            # (i, len(arr)-1]区间内是单调递减的
            j = len(arr)-1
            # 找到下一个比arr[i]要大的数
            while j>=0 and arr[i] >= arr[j]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            l = i+1
            r = len(arr)-1
            # 由单调递减变为单调递增
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            res.append("".join(arr))
            nextPermutation(arr)

        arr = list(s)
        arr.sort()
        res.append("".join(arr))
        nextPermutation(arr)
        return res


if __name__ == '__main__':
    print(Solution().permutation("abc"))