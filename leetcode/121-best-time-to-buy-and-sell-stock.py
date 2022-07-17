# first solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        r = 0
        l_stack, r_stack = [prices[0]], []
        l_min, r_max = prices[0], 0
        i = len(prices) - 1
        while i > 0:
            r_max = max(r_max, prices[i])
            r_stack.append(r_max)
            i -= 1
        j = 1
        while j < len(prices):
            r = max(r_stack[-1] - l_stack[-1], r)
            l_min = min(l_min, prices[j])
            l_stack.append(l_min)
            r_stack.pop()
            j += 1
        return r
