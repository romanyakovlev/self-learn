# first solution

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d_map = dict()
        d_set = set()
        for i in range(len(s)):
            if s[i] not in d_map.keys():
                if t[i] in d_set:
                    return False
                d_map[s[i]] = t[i]
                d_set.add(t[i])
            elif d_map[s[i]] != t[i]:
                return False
        return True
