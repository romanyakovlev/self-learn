
class Solution:
    def recurse(self, y, l):
        if len(l) == self.n:
            self.combs.append(l)
            return
        for x in range(self.n):
            for x1, y1 in l:
                if x1 == x or x1 + (y - y1) == x or x1 - (y - y1) == x:
                    break
            else:
                self.recurse(y + 1, l + [[x, y]])

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.combs = []
        result = []
        self.recurse(0, [])
        for l in self.combs:
            s = [["." for _ in range(n)] for _ in range(n)]
            for x, y in l:
                s[x][y] = "Q"
            result.append(["".join(k) for k in s])
        return result
        
        
