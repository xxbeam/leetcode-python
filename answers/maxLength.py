# 1239. 串联字符串的最大长度

class Solution:
    def maxLength(self, arr: list[str]) -> int:
        nums = []
        res = 0

        def addStr(i, num):
            if i == len(nums):
                nonlocal res
                res = max(res, bin(num).count("1"))
                return
            if num & nums[i] == 0:
                addStr(i+1, num | nums[i])
            addStr(i+1, num)

        for s in arr:
            num = 0
            for i in s:
                idx = ord(i) - ord("a")
                if num & (1 << idx) != 0:
                    num = 0
                    break
                num |= (1 << idx)
            if num > 0:
                nums.append(num)

        addStr(0, 0)
        return res


if __name__ == '__main__':
    print(Solution().maxLength(["un", "iq", "ue"]))
    print(Solution().maxLength(["cha", "r", "act", "ers"]))
    print(Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))
