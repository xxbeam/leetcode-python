# 1818. 绝对差值和

class Solution:
    def minAbsoluteSumDiff(self, nums1: list[int], nums2: list[int]) -> int:
        num_set = set()
        for i in range(len(nums1)):
            num_set.add(nums1[i])
        res = 0
        temp = 0
        for i in range(len(nums1)):
            x = abs(nums1[i]-nums2[i])
            res += x
            j = 0
            while j < x:
                if nums2[i] + j in num_set or nums2[i] - j in num_set:
                    temp = max(temp, x - j)
                    break
                j += 1
        return (res - temp) % (10 ** 9 + 7)


if __name__ == '__main__':
    print(Solution().minAbsoluteSumDiff([1,7,5], [2,3,5]))
    print(Solution().minAbsoluteSumDiff([2,4,6,8,10], [2,4,6,8,10]))
    print(Solution().minAbsoluteSumDiff([1,10,4,4,2,7], [9,3,5,1,7,4]))