# 1104. 二叉树寻路


class Solution:

    """
    计算出所属的行,向上查询，转换成正向顺序，然后判断行数奇偶，看需不需要反转
    """
    def pathInZigZagTree(self, label: int) -> list[int]:
        row = 0
        k = label
        while k > 0:
            k = k // 2
            row += 1
        if row % 2 == 0:
            label = ((2 ** row) - 1) - label + (2 ** (row - 1))
        path = []
        while row > 0:
            if row % 2 == 0:
                path.append(((2 ** row) - 1) - label + (2 ** (row - 1)))
            else:
                path.append(label)
            label = label // 2
            row -= 1
        return path[-1::-1]


if __name__ == '__main__':
    print(Solution().pathInZigZagTree(14))
    print(Solution().pathInZigZagTree(26))

