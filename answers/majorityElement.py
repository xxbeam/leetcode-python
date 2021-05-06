# 169. 多数元素

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        temp = -1
        count = 0
        for i in nums:
            if count == 0:
                temp = i
                count = 1
            else:
                if i == temp:
                    count += 1
                else:
                    count -= 1
        return temp

if __name__ == '__main__':
    print(Solution().majorityElement([6,5,5]))