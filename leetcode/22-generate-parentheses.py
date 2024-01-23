class Solution:

    def dfs(self, s, l, r):
        if len(s) == self.n * 2:
            self.l.append(s)
            return
        if l < self.n:
            self.dfs(s + "(", l + 1, r)
        if l > r:
            self.dfs(s + ")", l, r + 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.l = []
        self.n = n
        self.dfs("", 0, 0)
        return self.l
