# first solution - two pointers approach

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        last_index = len(nums) - 1
        left, right = 0, last_index
        # get first unsorted item from left
        while left < last_index:
            if nums[left] > nums[left + 1]:
                # move pointer back if there was equal items - from left
                while left > 0 and nums[left] == nums[left - 1]:
                    left -= 1
                break
            left += 1
        # no unsorted items
        if left == last_index:
            return 0
        # get first unsorted item from right
        while right > 0:
            if nums[right] < nums[right - 1]:
                # move pointer back if there was equal items - from right
                while right < last_index and nums[right] == nums[right + 1]:
                    right += 1
                break
            right -= 1
        unsorted_min, unsorted_max = min(nums[left:right + 1]), max(nums[left:right + 1])
        # find required items to sort from left and right
        while left != 0 and unsorted_max > nums[left - 1] and unsorted_min < nums[left - 1]:
            left -= 1
        while right != last_index and unsorted_max > nums[right + 1] and unsorted_min < nums[right + 1]:
            right += 1
        return right - left + 1
        
