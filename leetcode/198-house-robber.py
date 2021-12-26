class Solution:
    def rob(self, nums: List[int]) -> int:
        evens, odds = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                evens = max(evens + nums[i], odds)
            else:
                odds = max(odds + nums[i], evens)
        return max(evens, odds)
            
        
