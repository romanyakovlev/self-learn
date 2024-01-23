class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = 0
        for x in reversed(nums[:-1]):
            k += 1
            if x >= k:
                k = 0
        if k == 0:
            return True
        else:
            return False
