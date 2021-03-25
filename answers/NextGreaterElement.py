# 496. 下一个更大元素 I

class Solution:


    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        num_map = {}
        for idx, i in enumerate(nums2):
            while stack and nums2[stack[-1]] < i:
                num_map[nums2[stack.pop()]] = i
            stack.append(idx)
        while stack:
            num_map[nums2[stack.pop()]] = -1
        result = []
        for i in nums1:
            result.append(num_map.get(i))
        return result


if __name__ == '__main__':
    Solution().nextGreaterElement([4,1,2],[1,3,4,2])
