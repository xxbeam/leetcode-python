# 面试题 17.14. 最小K个数

class Solution:

    def smallestK(self, arr: list[int], k: int) -> list[int]:
        def partition(arr, l, r):
            mid = l + (r - l) // 2
            idx = l
            max_num = max(arr[l], arr[r], arr[mid])
            min_num = min(arr[l], arr[r], arr[mid])
            if arr[mid] != max_num and arr[mid] != min_num:
                idx = mid
            elif arr[r] != max_num and arr[r] != min_num:
                idx = r
            arr[idx], arr[r] = arr[r], arr[idx]
            p = l
            i = l
            while i < r:
                if arr[i] < arr[r]:
                    arr[i], arr[p] = arr[p], arr[i]
                    p += 1
                i += 1
            arr[r], arr[p] = arr[p], arr[r]
            return p

        def sorted(arr, l, r):
            p = partition(arr, l, r)
            if p == k:
                return
            if p > k:
                sorted(arr, l, p-1)
            else:
                sorted(arr, p+1, r)
        if k == 0:
            return []
        n = len(arr)
        if k >= n:
            return arr
        sorted(arr, 0, n-1)
        print(arr)
        return arr[:k]


if __name__ == '__main__':
    print(Solution().smallestK([1,3,5,7,2,4,6,8], 4))
    print(Solution().smallestK([62577,-220,-8737,-22,-6,59956,5363,-16699,0,-10603,64,-24528,-4818,96,5747,2638,-223,37663,-390,35778,-4977,-3834,-56074,7,-76,601,-1712,-48874,31,3,-9417,-33152,775,9396,60947,-1919,683,-37092,-524,-8,1458,80,-8,1,7,-355,9,397,-30,-21019,-565,8762,-4,531,-211,-23702,3,3399,-67,64542,39546,52500,-6263,4,-16,-1,861,5134,8,63701,40202,43349,-4283,-3,-22721,-6,42754,-726,118,51,539,790,-9972,41752,0,31,-23957,-714,-446,4,-61087,84,-140,6,53,-48496,9,-15357,402,5541,4,53936,6,3,37591,7,30,-7197,-26607,202,140,-4,-7410,2031,-715,4,-60981,365,-23620,-41,4,-2482,-59,5,-911,52,50068,38,61,664,0,-868,8681,-8,8,29,412], 131))

