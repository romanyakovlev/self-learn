class Solution:
    d = {
                     "2": "abc", "3": "def",
        "4": "ghi",  "5": "jkl", "6": "mno",
        "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    def dfs(self, r: list[str], i: int):
        if i >= len(self.digits):
            if r:
                self.l.append(r)
            return
        for letter in self.d[self.digits[i]]:
            self.dfs(r + letter, i + 1)

    def letterCombinations(self, digits: str) -> List[str]:
        self.l = []
        self.digits = digits
        self.dfs("", 0)
        return self.l
