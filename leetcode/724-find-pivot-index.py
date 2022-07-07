class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i = 0
        s1, s2 = 0, sum(nums[1:])
        while i + 1 < len(nums):
            if s1 == s2:
                break
            s1 += nums[i]
            s2 -= nums[i + 1]
            i += 1
        return -1 if s1 != s2 else i

# or 

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s1, s2 = 0, sum(nums[1:])
        if s1 == s2:
            return 0
        for j in range(len(nums) - 1):
            s1 += nums[j]
            s2 -= nums[j + 1]
            if s1 == s2:
                return j + 1
        return -1

# solition from leetcode 

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # Initialization:
        # Left hand side be empty, and
        # Right hand side holds all weights.
        total_weight_on_left, total_weight_on_right = 0, sum(nums)

        for idx, current_weight in enumerate(nums):

            total_weight_on_right -= current_weight

            if total_weight_on_left == total_weight_on_right:
                # balance is met on both sides
                # i.e., sum( nums[ :idx] ) == sum( nums[idx+1: ] )
                return idx

            total_weight_on_left += current_weight

        return -1
