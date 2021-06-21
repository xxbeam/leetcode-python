# 401. 二进制手表


class Solution:

    """
    转换为0-1背包问题
    """
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        res = []
        m = [1,2,4,8,16,32,0,0,0,0]
        h = [0,0,0,0,0,0,1,2,4,8]
        def addTime(min_now, hour_now, idx, turnedOn):
            if min_now > 59 or hour_now > 11:
                return
            if turnedOn == 0:
                if min_now < 10:
                    time = str(hour_now) + ":0" + str(min_now)
                else:
                    time = str(hour_now) + ":" + str(min_now)
                res.append(time)
                return
            for i in range(idx, 10):
                addTime(min_now+m[i], hour_now+h[i], i+1, turnedOn-1)
        addTime(0, 0, 0, turnedOn)
        return res

if __name__ == '__main__':
    print(Solution().readBinaryWatch(3))
    print(Solution().readBinaryWatch(1))