# 20. 有效的括号

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        dict = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in s:
            if i == "{" or i == "(" or i == "[":
                stack.append(i)
            else:
                if stack:
                    temp = stack.pop()
                    if temp != dict.get(i):
                        return False
                else:
                    return False
        if stack:
            return False
        return True



if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"))

