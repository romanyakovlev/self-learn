# 1st solution

class Solution:

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        r = []
        i1, i2 = 0, 0
        while i1 < len(firstList) and i2 < len(secondList):
            a, b = firstList[i1], secondList[i2]
            if a[1] < b[0]:
                i1 += 1
            elif b[1] < a[0]:
                i2 += 1
            elif a[1] > b[1]:
                r.append([max(a[0], b[0]), b[1]])
                i2 += 1
            else:
                r.append([max(a[0], b[0]), a[1]])
                i1 += 1
        return r
 
