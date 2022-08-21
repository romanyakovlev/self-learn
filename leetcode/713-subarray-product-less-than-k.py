# first solution

class Solution:
  
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        win_size = 1
        win_prod = 1
        left = 0
        counter = 0
        while (right := (win_size + left - 1)) < len(nums):
            win_prod *= nums[right]
            if nums[right] < k:
                counter += 1
            while win_prod >= k and win_size > 1:
                win_prod /= nums[left]
                win_size -= 1
                left += 1
            counter += win_size - 1
            win_size += 1
        return counter
