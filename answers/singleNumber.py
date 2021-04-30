# 137. 只出现一次的数字 II


class Solution:


    '''
        0 ^ x = x,

        x ^ x = 0；

        x & ~x = 0,

        x & ~0 =x;
        x第一次出现后，a = (a ^ x) & ~b的结果为 a = x, b = (b ^ x) & ~a的结果为此时因为a = x了，所以b = 0。

        x第二次出现：a = (a ^ x) & ~b, a = (x ^ x) & ~0, a = 0; b = (b ^ x) & ~a 化简， b = (0 ^ x) & ~0 ,b = x;

        x第三次出现：a = (a ^ x) & ~b， a = (0 ^ x) & ~x ,a = 0; b = (b ^ x) & ~a 化简， b = (x ^ x) & ~0 , b = 0;所以出现三次同一个数，a和b最终都变回了0.
    '''
    def singleNumber(self, nums: list[int]) -> int:
        a, b = 0, 0
        for i in nums:
            a = (a ^ i) & ~b
            b = (b ^ i) & ~a
        return a

if __name__ == '__main__':
    print(Solution().singleNumber([2,2,3,2]))
    # print(3>>3>>3)