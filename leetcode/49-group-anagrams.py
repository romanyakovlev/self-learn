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
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            sorted_s = self.mergeSort(s)
            if sorted_s not in d.keys():
                d[sorted_s] = [s]
            else:
                d[sorted_s].append(s)
        return list(d.values())
