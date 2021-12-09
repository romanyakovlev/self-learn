class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while (nums[l] + nums[r]) != target:
            if abs((nums[l] + nums[r-1]) - target) > abs((nums[l+1] + nums[r]) - target):
                l += 1
            else:
                r -= 1
        return [l+1, r+1]
