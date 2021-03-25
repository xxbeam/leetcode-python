# 844. 比较含退格的字符串

class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:
        S1 = []
        T1 = []
        for i in S:
            if i == "#":
                if S1:
                    S1.pop()
            else:
                S1.append(i)

        for i in T:
            if i == "#":
                if T1:
                    T1.pop()
            else:
                T1.append(i)
        return S1 == T1
