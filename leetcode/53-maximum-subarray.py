class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m, c = nums[0], nums[0]
        for x in nums[1:]:
            if c < 0:
                c = x
            else:
                c += x
            if c > m:
                m = c  
        return m

# todo: make divide and conquer solution
