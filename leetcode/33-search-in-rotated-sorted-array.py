class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            i = l + (r - l) // 2
            if nums[i] == target:
                return i
            elif nums[i] > target:
              # when nums[i] > nums[r] - it means list has pivot
              # if its true - then we need to define in which part of list target can 
              # if target < nums[l] - left side does not have target element for sure
              # otherwise - right side
                if nums[i] > nums[r] and target < nums[l]:
                    l = i + 1
                else:
                    r = i - 1
            elif nums[i] < target:
                # same logic applies here
                if nums[i] < nums[l] and target > nums[r]:
                    r = i - 1
                else:
                    l = i + 1
        return -1

# from leetcode discussion
 
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
