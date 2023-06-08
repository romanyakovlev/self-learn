# 1st solution (using 2 heaps pattern)

from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        h_capital, h_profits = [], []
        for i, v in enumerate(capital):
            heappush(h_capital, (v, i))
        for _ in range(k):
            while h_capital and h_capital[0][0] <= w:
                index = heappop(h_capital)[1]
                heappush(h_profits, -profits[index])
            if h_profits:
                w -= heappop(h_profits)
        return w
