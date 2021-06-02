# 1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？


class Solution:
    def canEat(self, candiesCount: list[int], queries: list[list[int]]) -> list[bool]:
        total_candies = [0]
        for i in candiesCount:
            total_candies.append(i + total_candies[-1])
        res = []
        for arr in queries:
            min_candies = arr[1] + 1
            max_candies = (arr[1] + 1) * arr[2]
            if max_candies <= total_candies[arr[0]] or min_candies > total_candies[arr[0]+1]:
                res.append(False)
            else:
                res.append(True)
        return res


if __name__ == '__main__':
    print(Solution().canEat([7, 4, 5, 3, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]))
    print(Solution().canEat([5, 2, 6, 4, 1], [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]))
    print(Solution().canEat([7, 11, 5, 3, 8], [[2, 2, 6], [4, 2, 4], [2, 13, 1000000000]]))

