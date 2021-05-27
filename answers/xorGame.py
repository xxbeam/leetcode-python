# 810. 黑板异或游戏


class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        res = 0
        for i in nums:
            res = res ^ i
        # 当数组异或不为0时，总有最优解能消除所有数组，则最后一个消除者为输家
        return res == 0 or len(nums) % 2 == 0


if __name__ == '__main__':
    print(Solution().xorGame([1, 2, 3]))
    print(Solution().xorGame([1, 1, 2]))
