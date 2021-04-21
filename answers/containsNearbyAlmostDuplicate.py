# 220. 存在重复元素 III


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        if len(nums) < 2 or k == 0:
            return False
        num_map = {}
        for i in range(len(nums)):
            if nums[i] in num_map:
                num_map.get(nums[i]).append(i)
            else:
                num_map[nums[i]] = [i]
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + t >= nums[j]:
                    arr1 = num_map.get(nums[i])
                    arr2 = num_map.get(nums[j])
                    for x in range(len(arr1)):
                        for y in range(len(arr2)):
                            if arr1[x] == arr2[y]:
                                continue
                            if abs(arr1[x] - arr2[y]) <= k:
                                return True
                else:
                    break
        return False


if __name__ == '__main__':
    print(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))