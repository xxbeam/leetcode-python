# 1736. 替换隐藏数字得到的最晚时间

class Solution:
    def maximumTime(self, time: str) -> str:
        res = ""
        for i in range(len(time)):
            s = time[i]
            if s == "?":
                if i == 0:
                    if time[1] != "?" and time[1] >= '4':
                        s = '1'
                    else:
                        s = '2'
                elif i == 1:
                    if res[0] == "2":
                        s = '3'
                    else:
                        s = '9'
                elif i == 3:
                    s = '5'
                elif i == 4:
                    s = '9'
            res += s
        return res



if __name__ == '__main__':
    # print(Solution().maximumTime("2?:?0"))
    # print(Solution().maximumTime("0?:3?"))
    # print(Solution().maximumTime("1?:22"))
    print(Solution().maximumTime("??:3?"))