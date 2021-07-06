# 726. 原子的数量


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [{}]
        i = 0

        def praseInt():
            nonlocal i
            j = i
            while j < len(formula) and 0 <= ord(formula[j]) - ord('0') < 10:
                j += 1
            num = 1
            if i < j:
                num = int(formula[i: j])
            i = j
            return num

        def praseAtom():
            nonlocal i
            j = i + 1
            while j < len(formula) and 0 <= ord(formula[j]) - ord('a') < 26:
                # 是小写字母
                j += 1
            atom = formula[i: j]
            i = j
            return atom

        while i < len(formula):
            if formula[i] == '(':
                stack.append({})
                i += 1
            elif formula[i] == ')':
                atom_map1 = stack.pop()
                atom_map = stack[-1]
                i += 1
                num = praseInt()
                for s in atom_map1.keys():
                    if s not in atom_map:
                        atom_map[s] = 0
                    atom_map[s] += atom_map1[s] * num
            else:
                atom = praseAtom()
                num = praseInt()
                atom_map = stack[-1]
                if atom not in atom_map:
                    atom_map[atom] = 0
                atom_map[atom] += num

        arr = list(stack[-1].keys())
        arr.sort()
        res = ""
        for s in arr:
            res += s
            if atom_map[s] > 1:
                res += str(atom_map[s])
        return res


if __name__ == '__main__':

    print(Solution().countOfAtoms("Mg(OH)2"))
    print(Solution().countOfAtoms("K4(ON(SO3)2)2"))
    print(Solution().countOfAtoms("H11He49NO35B7N46Li20"))