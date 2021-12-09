class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        zeros = 0
        while True:
            while (x + zeros) < len(nums) and nums[x + zeros] == 0:
                zeros += 1
            if (x + zeros) >= len(nums):
                break
            nums[x], nums[x + zeros] = nums[x + zeros], nums[x]
            x += 1
