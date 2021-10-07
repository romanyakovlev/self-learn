# solution using recursion+func result caching (also success from 1st attempt - yay :D)

class Solution:
    def count_entries(self, k):
        if self.n == k:
            return 1
        elif self.n < k:
            return 0
        else:
            if k + 1 not in self.d.keys():
                self.d[k + 1] = self.count_entries(k + 1)
            if k + 2 not in self.d.keys():
                self.d[k + 2] = self.count_entries(k + 2)
            return self.d[k + 1] + self.d[k + 2]
    
    def climbStairs(self, n: int) -> int:
        self.n = n
        self.d = dict()
        return self.count_entries(1) + self.count_entries(2) 
        
