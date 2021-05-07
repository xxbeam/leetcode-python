# 32. 最长有效括号


class Solution:
    # 根据无法匹配的括号所在位置 计算长度
    def longestValidParentheses(self, s: str) -> int:
            stack = []
            l = 0
            for i in range(len(s)):
                if s[i] == "(":
                    stack.append(i)
                else:
                    if stack and s[stack[-1]] == "(":
                        stack.pop()
                        if stack:
                            l = max(i - stack[-1], l)
                        else:
                            l = max(i+1, l)
                    else:
                        if stack:
                            l = max(i-stack[-1]-1, l)
                        else:
                            l = max(i, l)
                        stack.append(i)
            if not stack:
                return len(s)
            return l


if __name__ == '__main__':
    print(Solution().longestValidParentheses("(()()"))
    print(Solution().longestValidParentheses("()(()"))
    print(Solution().longestValidParentheses("(()"))
    print(Solution().longestValidParentheses("(())"))

