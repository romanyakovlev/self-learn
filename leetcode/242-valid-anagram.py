# first solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = dict()
        for n in s:
            if n in d.keys():
                d[n] += 1
            else:
                d[n] = 1
        for n in t:
            if n in d.keys() and d[n] > 0:
                d[n] -= 1
            else:
                return False
        return True
