# first solution

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        r = 0
        one_val = 0
        for c in s:
            d[c] = d.get(c, 0) + 1
        for v in d.values():
            r += (v // 2) * 2
            if one_val == 0 and v % 2 != 0:
                one_val += 1
        return r + one_val
