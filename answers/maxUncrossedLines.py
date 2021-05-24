# 1035. 不相交的线

class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        size1 = len(nums1)
        size2 = len(nums2)
        dp = []
        for i in range(size2):
            dp.append([0] * (size1 + 1))
        for i in range(size1):
            if nums1[i] == nums2[0]:
                dp[0][i+1] = 1
            else:
                dp[0][i+1] = dp[0][i]
        for i in range(1, size2):
            for j in range(size1):
                if nums2[i] == nums1[j]:
                    dp[i][j+1] = dp[i-1][j]+1
                else:
                    dp[i][j+1] = max(dp[i-1][j+1], dp[i][j])
        return dp[size2-1][size1]


if __name__ == '__main__':
    print(Solution().maxUncrossedLines([1,2,2,2,1,2],[1]))
    # print(Solution().maxUncrossedLines([2,5,1,2,5],[10,5,2,1,5,2]))
    # print(Solution().maxUncrossedLines([1,3,7,1,7,5],[1,9,2,5,1]))