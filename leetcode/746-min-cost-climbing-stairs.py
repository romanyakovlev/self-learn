# first solution

class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * len(cost)
        i = len(cost) - 1
        min_cost[i], min_cost[i - 1] = cost[i], cost[i - 1]
        i -= 2
        while i >= 0:
            if min_cost[i + 1] < min_cost[i + 2]:
                min_cost[i] = cost[i] + min_cost[i + 1]
            else: 
                min_cost[i] = cost[i] + min_cost[i + 2]
            i -= 1
        return min(min_cost[0], min_cost[1])
        
