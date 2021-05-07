# 150. 逆波兰表达式求值

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                stack.append(stack.pop(-2) - stack.pop(-1))
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                stack.append(int(stack.pop(-2) / stack.pop(-1)))
            else:
                stack.append(int(i))
        return stack.pop()

if __name__ == '__main__':
    print(Solution().evalRPN(["4","13","5","/","+"]))