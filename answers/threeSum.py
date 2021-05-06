# 15. 三数之和

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []
        arr = []
        # 排序
        nums.sort()
        size = len(nums)
        for i in range(size-2):
            # 跳过重复的第一位
            if nums[i] == nums[i-1] and i > 0:
                continue
            j, k = i+1, size-1
            while j < k:
                t = nums[i] + nums[j] + nums[k]
                # 如果比0大，说明第三位数大了，否则第二位数小了
                if t > 0:
                    k -= 1
                elif t < 0:
                    j += 1
                else:
                    arr.append([nums[i], nums[j], nums[k]])
                    # 取下一个与当前nums[j], nums[k]不等的数
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return arr

if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,2,-1,-4]))