# 682. 棒球比赛

class Solution:

    def calPoints(self, ops: list[str]) -> int:
        if not ops:
            return 0
        scores = []
        for i in ops:
            if i == "+":
                scores.append(sum(scores[-2:]))
            elif i == "D":
                scores.append(2 * scores[-1])
            elif i == "C":
                scores.pop()
            else:
                scores.append(int(i))
        return sum(scores)
