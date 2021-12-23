class Solution:
    def recurse(self, i, low, up):
        if i <= len(self.a_l) - 1:
            a_i = self.a_l[i]
            self.recurse(i + 1, low + [a_i], up)
            self.recurse(i + 1, low, up + [a_i])
        else:
            l = self.o_l.copy()
            for x in low:
                l[x] = l[x].lower()
            for x in up:
                l[x] = l[x].upper()
            self.l.append(''.join(l))
    
    def letterCasePermutation(self, s: str) -> List[str]:
        self.l = []
        self.a_l = [i for i, x in enumerate(s) if x.isalpha()]
        self.o_l = list(s)
        self.recurse(0, [], [])
        return self.l
