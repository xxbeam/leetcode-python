# 1833. 雪糕的最大数量

class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        # 计算排序 O(n)
        arr = [0] * (max(costs)+1)
        for i in costs:
            arr[i] += 1
        res = 0
        for i in range(1, len(arr)):
            if arr[i] == 0:
                continue
            if coins < i:
                break
            if coins >= i * arr[i]:
                num = arr[i]
            else:
                num = coins//i
            coins -= i * num
            res += num
        return res


if __name__ == '__main__':
    print(Solution().maxIceCream([1,3,2,4,1], 7))
    print(Solution().maxIceCream([10,6,8,7,7,8], 5))
    print(Solution().maxIceCream([1,6,3,1,2,5], 20))