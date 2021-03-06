# first solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        r = 0
        l_stack, r_stack = [prices[0]], [prices[-1]]
        l_min, r_max = prices[0], 0
        i = len(prices) - 2
        while i > 0:
            r_stack.append(max(r_stack[-1], prices[i]))
            i -= 1
        j = 1
        while j < len(prices):
            r = max(r_stack[-1] - l_stack[-1], r)
            l_stack.append(min(l_stack[-1], prices[j]))
            r_stack.pop()
            j += 1
        return r

# optimized first solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        r = 0
        r_stack = [prices[-1]]
        l_min = prices[0]
        i = len(prices) - 2
        while i > 0:
            r_stack.append(max(r_stack[-1], prices[i]))
            i -= 1
        i = 1
        while i < len(prices):
            r = max(r_stack[-1] - l_min, r)
            l_min = min(l_min, prices[i])
            r_stack.pop()
            i += 1
        return r

    
# solution from disc

class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit

# second solution from disc

def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

# third

# The heuristic is that as long as current price is higher than previous lowest price, 
# max profit could be updated. So I use buy to track previous lowest price 
# (indicating we can buy in that time) and ans to track max profit we have achieved so far.

def maxProfit(prices):
	buy, ans = float('inf'), 0
	for p in prices:
		buy, ans = min(buy, p), max(ans, p-buy)
	return ans


