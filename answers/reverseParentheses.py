# 1190. 反转每对括号间的子串


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ")":
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack += temp
            else:
                stack.append(i)
        return "".join(stack)


if __name__ == '__main__':
    print(Solution().reverseParentheses("(abcd)"))
    print(Solution().reverseParentheses("(u(love)i)"))
    print(Solution().reverseParentheses("(ed(et(oc))el)"))
    print(Solution().reverseParentheses("a(bcdefghijkl(mno)p)q"))
    arr = ["1","a","b"]
    print("".join(arr))