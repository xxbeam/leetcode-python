# 165. 比较版本号


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n = len(version1)
        m = len(version2)
        i, j = 0, 0
        while i < n or j < m:
            x = 0
            while i < n and version1[i] != ".":
                x = x * 10 + int(version1[i])
                i += 1
            i += 1
            y = 0
            while j < m and version2[j] != ".":
                y = y * 10 + int(version2[j])
                j += 1
            j += 1
            if x != y:
                return 1 if x > y else -1
        return 0


if __name__ == '__main__':
    print(Solution().compareVersion("1.01", "1.001"))
    print(Solution().compareVersion("1.0", "1.0.0"))
    print(Solution().compareVersion("0.1", "1.1"))
    print(Solution().compareVersion("1.0.1", "1"))
    print(Solution().compareVersion("7.5.2.4", "7.5.3"))
