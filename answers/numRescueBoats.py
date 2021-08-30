# 881. 救生艇

class Solution:

    def numRescueBoats(self, people: list[int], limit: int) -> int:
        res = 0
        people.sort()
        l = 0
        r = len(people) - 1
        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            res += 1
        if l == r:
            res += 1
        return res


if __name__ == '__main__':
    print(Solution().numRescueBoats([3,2,3,2,2], 6))
    print(Solution().numRescueBoats([1,2], 3))
    print(Solution().numRescueBoats([3,2,2,1], 3))
    print(Solution().numRescueBoats([3,5,3,4], 5))