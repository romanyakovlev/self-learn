class Solution:
    d = {}
    
    def fib(self, n: int) -> int:
        if n in self.d.keys():
            return self.d[n]
        if n <= 1:
            return n
        f_n = self.fib(n-1) + self.fib(n-2)
        if f_n not in self.d.keys():
            self.d[n] = f_n
        return f_n
