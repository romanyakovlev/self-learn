# first solution

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float("inf")
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            right = len(nums) - 1
            left = i + 1
            fixed_num = nums[i]
            while left < right:
                value = nums[left] + nums[right] + fixed_num
                if value < target:
                    left += 1
                elif value > target:
                    right -= 1
                else:
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                if abs(value - target) < abs(closest - target):
                    closest = value
        return closest
                
