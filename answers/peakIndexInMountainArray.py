# 852. 山脉数组的峰顶索引


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = (l+r) >> 1
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] > arr[mid]:
                r = mid
            else:
                l = mid + 1


if __name__ == '__main__':
    print(Solution().peakIndexInMountainArray([0,1,0]))
    print(Solution().peakIndexInMountainArray([0,2,1,0]))
    print(Solution().peakIndexInMountainArray([0,10,5,2]))
    print(Solution().peakIndexInMountainArray([3,4,5,1]))
    print(Solution().peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))