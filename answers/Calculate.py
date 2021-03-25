# 224. 基本计算器

class Solution:

    def cal(self, a: int, b: int, operator: str):
        if operator == "+":
            return b + a
        else:
            return b - a

    def calculate(self, s: str) -> int:
        nums = []
        operators = []
        numStr = ""
        lastStr = ""
        for i in s:
            if i.isdigit():
                numStr += i
            else:
                temp = [i, numStr]
                numStr = ""
                while temp:
                    t = temp.pop()
                    if t == " " or t == "":
                        continue
                    elif t == "+" or t == "-":
                        if not nums or lastStr == "(":
                            nums.append(0)
                            operators.append(t)
                        else:
                            operators.append(t)
                    elif t == "(":
                        operators.append(t)
                    elif t == ")":
                        isFirst = True
                        while operators:
                            if operators[-1] == "(":
                                if isFirst:
                                    operators.pop()
                                    isFirst = False
                                else:
                                    break
                            else:
                                nums.append(self.cal(nums.pop(), nums.pop(), operators.pop()))
                    else:
                        nums.append(int(t))
                        while operators:
                            if operators[-1] != "(":
                                nums.append(self.cal(nums.pop(), nums.pop(), operators.pop()))
                            else:
                                break

            lastStr = i
        if numStr != "":
            nums.append(int(numStr))
        while operators:
            nums.append(self.cal(nums.pop(), nums.pop(), operators.pop()))
        return nums.pop()


if __name__ == '__main__':

    print(Solution().calculate("(7)-(0)+(4)"))