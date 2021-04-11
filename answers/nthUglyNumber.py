# 264. 丑数 II


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [1]
        idx1 = 0
        idx2 = 0
        idx3 = 0
        for i in range(n-1):
            num1 = arr[idx1]*2
            num2 = arr[idx2]*3
            num3 = arr[idx3]*5
            min_num = min(num1, num2, num3)
            arr.append(min_num)
            if num1 == min_num:
                idx1 += 1
            if num2 == min_num:
                idx2 += 1
            if num3 == min_num:
                idx3 += 1
        return arr[-1]


if __name__ == '__main__':
    nums_map = {}
    print(nums_map.get(22))