# first solution

class Solution:
    def isValid(self, s: str) -> bool:
        par_in = {'(', '{', '['}
        d_out = {')':'(', '}':'{', ']':'['}
        l = []
        index = 0
        while len(s) > index:
            x = s[index]
            if x in par_in:
                l.append(x)
            else:
                if len(l) == 0 or l[-1] != d_out[x]:
                    return False
                else:
                    l.pop()
            index += 1
        return True if len(l) == 0 else False
  
#second solution
class Solution:
    p_map = {'(': ')', '{': '}', '[': ']'}
    
    def isValid(self, s: str) -> bool:
        l = []
        for p in s:
            if p in self.p_map.keys():
                l.append(p)
            elif l and self.p_map[l[-1]] == p:
                l.pop()
            else:
                return False
        return len(l) == 0


# more beautiful - from leetcode discussion

class Solution(object):
    def isValid(self, s):
        d = {'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False
        return len(stack) == 0
