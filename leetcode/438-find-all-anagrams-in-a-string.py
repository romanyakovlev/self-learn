# first solution

# the idea is to use sliding window to save dict with data about characters 
# when window moves to right: 
# 1. left old char is being deleted from dict
# 2. right new char is being added to dict
# with this feature we can save dict state wihout it recreation, which is very fast

class Solution:
    
    def createDict(self, s: str) -> dict:
      
        d = dict()
        for c in s:
            d[c] = d.get(c, 0) + 1
        return d

    def modifySlidingDict(self, i: int, d_s: dict, s: str, p: str) -> None:
        prev_i = i - 1
        next_i = prev_i + len(p)
        d_s[s[prev_i]] -= 1
        if d_s[s[prev_i]] == 0:
            del d_s[s[prev_i]]
        d_s[s[next_i]] = d_s.get(s[next_i], 0) + 1
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = 0
        indexes_list = []
        d_t = self.createDict(p)
        d_s = None
        len_diff = len(s) - len(p)
        while i <= len_diff:
            if d_s is not None:
                self.modifySlidingDict(i, d_s, s, p)
            else:
                d_s = self.createDict(s[i:i + len(p)])
            if d_s == d_t:
                indexes_list.append(i)
            i += 1
        return indexes_list
