class Solution:

    def isSubsetSum (self, N, arr, sum):
        arr.sort()
        s = {0}
        for x in arr:
            if x > sum:
                return 0
            s = s | {y+x for y in s if y+x <= sum}
            if sum in s:
                return 1
        return 0
