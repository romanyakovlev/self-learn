# first solution

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            i = l + (r - l) // 2
            if nums[i] == target:
                return True
            elif nums[l] == nums[r]:
                if nums[l] == target:
                    return True
                r -= 1
                l += 1
            elif nums[i] > target:
                if nums[i] > nums[r] and target < nums[l]:
                    l = i + 1
                else:
                    r = i - 1
            else:
                if nums[i] < nums[l] and target > nums[r]:
                    r = i - 1
                else:
                    l = i + 1
        return False
