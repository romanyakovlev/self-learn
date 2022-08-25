# first solution

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target1 = target - nums[i]
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target2 = target1 - nums[j]
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == target2:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                            l += 1
                        while r > 0 and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < target2:
                        l += 1
                    else:
                        r -= 1
        return result
