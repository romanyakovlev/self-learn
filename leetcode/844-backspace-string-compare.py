# first solution - using stack

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
        
# second solution - using two pointers

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i1, i2 = len(s) - 1, len(t) - 1
        c1, c2 = 0, 0
        while i1 >= 0 or i2 >= 0:
            j1, j2 = None, None
            while i1 >= 0:
                if s[i1] == '#':
                    c1 += 1
                    i1 -= 1
                    while c1 != 0 and i1 >= 0:
                        if s[i1] == '#':
                            c1 += 1
                        else:
                            c1 -= 1
                        i1 -= 1
                else:
                    j1 = i1
                    i1 -= 1
                    break
            while i2 >= 0:
                if t[i2] == '#':
                    c2 += 1
                    i2 -= 1
                    while c2 != 0 and i2 >= 0:
                        if t[i2] == '#':
                            c2 += 1
                        else:
                            c2 -= 1
                        i2 -= 1
                else:
                    j2 = i2
                    i2 -= 1
                    break
            if (
                (j1 is not None and j2 is not None and s[j1] != t[j2]) or
                (j1 is None and j2 is not None) or
                (j2 is None and j1 is not None)
            ):
                return False
        return True
 
# solution from leetcode
        
class Solution:
    def getNextValidCharIndex(self, s, i):
        backspace = 0
        while i >= 0:
            if s[i] == '#':
                backspace += 1
            elif backspace > 0:
                backspace -= 1
            else:
                break
            i -= 1
        return i
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        index1, index2 = len(s) - 1, len(t) - 1
        while index1 >= 0 or index2 >= 0:
            i1 = self.getNextValidCharIndex(s, index1)
            i2 = self.getNextValidCharIndex(t, index2)
            if i1 < 0 and i2 < 0:
                return True
            elif i1 < 0 or i2 < 0:
                return False
            elif s[i1] != t[i2]:
                return False
            
            index1 = i1 - 1
            index2 = i2 - 1
        return True

