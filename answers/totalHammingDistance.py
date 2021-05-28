# 477. 汉明距离总和


class Solution:

    """
        统计每一bit的0的数量，然后与同位bit为1的数量相乘则为两两num比较，当前位不一样的总数
    """
    def totalHammingDistance(self, nums: list[int]) -> int:
        max_num = max(nums)
        l = len(bin(max_num))-2
        arr = [0] * l
        for i in nums:
            for j in range(l):
                if i & 1 << (l-1-j) == 0:
                    arr[j] += 1
        res = 0
        for i in arr:
            res += (i * (len(nums)-i))
        return res



if __name__ == '__main__':
    print(Solution().totalHammingDistance([4,14,2]))