# first algo

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = (len(nums) - 1) // 2
        r = [0, len(nums) - 1]
        while (r[1] - r[0]) > 1:
            if nums[index] == target:
                return index
            elif nums[index] > target:
                r[1] = index
                index = (r[1] + r[0]) // 2
            elif nums[index] < target:
                r[0] = index
                index = (r[1] + r[0]) // 2
        if nums[r[0]] >= target:
            return r[0]
        elif nums[r[1]] == target or (nums[r[0]] < target and target < nums[r[1]]):
            return r[1]
        else:
            return r[1] + 1

# another solution

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            i = (l + r) // 2
            if target > nums[i]:
                l = i + 1
            elif target < nums[i]:
                r = i - 1
            elif target == nums[i]:
                return i
        return l

# use bisect

import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)

# better binary search

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
