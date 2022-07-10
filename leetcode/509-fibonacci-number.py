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

# solution from leetcode 

class Solution:
    def fib(self, N: int) -> int:
    	a, b = 0, 1
    	for i in range(N): a, b = b, a + b
    	return a
