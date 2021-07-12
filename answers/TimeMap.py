# 981. 基于时间的键值存储


class TimeMap:
    time_map = {}
    def __init__(self):
        """
        Initialize your data structure here.
        """

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        value_arr = self.time_map[key]
        if timestamp >= value_arr[0][1]:
            l = 0
            r = len(value_arr)-1
            while l <= r:
                mid = l + (r - l) // 2
                if value_arr[mid][1] == timestamp:
                    return value_arr[mid][0]
                elif value_arr[mid][1] > timestamp:
                    r = mid - 1
                else:
                    l = mid + 1
            return value_arr[r][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)