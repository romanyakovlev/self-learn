# first solution

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i1, i2 = 0, 0
        l1, l2 = [], []
        while i1 < len(s):
            if s[i1] != '#':
                l1.append(s[i1])
            elif l1:
                l1.pop()
            i1 += 1
        while i2 < len(t):
            if t[i2] != '#':
                l2.append(t[i2])
            elif l2:
                l2.pop()
            i2 += 1
        return l1 == l2
        
