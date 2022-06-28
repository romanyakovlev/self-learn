# first solution
# use dict

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

# use sorting (slow but for practice)    
    
class Solution:
    def mergeSort(self, s: str) -> str:
        if len(s) <= 1:
            return s
        i = len(s) // 2
        s1 = self.mergeSort(s[:i])
        s2 = self.mergeSort(s[i:])
        s3 = ''
        s1_i, s2_i = 0, 0
        while s1_i < len(s1) and s2_i < len(s2):
            if s1[s1_i] <= s2[s2_i]:
                s3 += s1[s1_i]
                s1_i += 1
            else:
                s3 += s2[s2_i]
                s2_i += 1
        while s1_i < len(s1):
            s3 += s1[s1_i]
            s1_i += 1
        while s2_i < len(s2):
            s3 += s2[s2_i]
            s2_i += 1
        return s3

    def isAnagram(self, s: str, t: str) -> bool:
        return self.mergeSort(s) == self.mergeSort(t)
