# 1109. 航班预订统计

class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        ans = [0] * (n+1)
        for booking in bookings:
            ans[booking[0]-1] += booking[2]
            ans[booking[1]] -= booking[2]
        for i in range(1, n):
            ans[i] += ans[i-1]
        return ans[:n]


if __name__ == '__main__':
    print(Solution().corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5))
    print(Solution().corpFlightBookings([[1,2,10],[2,2,15]], 2))