# 65. 有效数字


class Solution:
    def isNumber(self, s: str) -> bool:
        # 先判断第一位是否有正负
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if not s:
            return False
        # 是否出现小数点
        point = False
        # 前缀是否是数字
        is_number = False
        for i in range(len(s)):
            if s[i].isdigit():
                is_number = True
            elif s[i] == '.' and not point:
                if not is_number and (i == len(s) - 1 or not s[i+1].isdigit()):
                    return False
                point = True
            elif is_number and (s[i] == 'e' or s[i] == 'E'):
                if i == len(s)-1:
                    # 如果e是最后一位
                    return False
                # 判断后面的数是否是整数
                temp = s[i+1:]
                if temp[0] == '+' or temp[0] == '-':
                    temp = temp[1:]
                if not temp or not temp.isdigit():
                    return False
                return True
            else:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isNumber("e9"))
    print(Solution().isNumber("53.5e93"))
    print(Solution().isNumber("-0.1"))
