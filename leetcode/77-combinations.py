class Solution:
    def recurse(self, n, l, c):
        c += 1
        for x in range(n, self.n_limit + 1):
            if c == self.k:
                self.end_l.append(l + [x])
            else:
                self.recurse(x + 1, l + [x], c)
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n_limit = n
        self.k = k
        self.end_l = []
        if self.k != 1:
            for x in range(1, self.n_limit + 1):
                self.recurse(x + 1, [x], 1)
            return self.end_l
        else:
            for x in range(1, self.n_limit + 1):
                self.end_l.append([x])
            return self.end_l
