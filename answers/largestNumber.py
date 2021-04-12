# 179. 最大数
import functools


class Solution:

    def largestNumber(self, nums: list[int]) -> str:
        arr = []
        for i in nums:
            arr.append(str(i))
        arr.sort(key=functools.cmp_to_key(my_compare))
        num_str = ""
        for s in arr:
            num_str += s
        # 处理0的情况 比如[0,0] 应该返回一个0
        while len(num_str) > 1:
            if num_str[0] == '0':
                num_str = num_str[1:]
            else:
                break
        return num_str


# 自定义排序规则
def my_compare(x: str, y: str):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    return 0



if __name__ == '__main__':
    Solution().largestNumber([10,3])