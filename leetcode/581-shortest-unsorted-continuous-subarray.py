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
        # find required items to sort from left and right and add them to unsorted list range
        while left != 0 and unsorted_max > nums[left - 1] and unsorted_min < nums[left - 1]:
            left -= 1
        while right != last_index and unsorted_max > nums[right + 1] and unsorted_min < nums[right + 1]:
            right += 1
        return right - left + 1

# solution from leetcode

# Idea: Find the first index violating the ascending order, and the first index violating the descending order from the end. 
# Our temporary window → [start, end]
# But sorting the window alone does not guarantee sorting the whole array. 
# We also need to extend to numbers before the window which are bigger than the minimum of window, 
# and extend to numbers after the window which are smaller than the maximum of the window.

def findUnsortedSubarray(nums):
	n = len(nums)
	start = 0
	end = n - 1
	
	# find first index violating ascending order
	while start < n - 1 and nums[start] <= nums[start+1]:
		start += 1

	# edge case: already sorted
	if start == n - 1:
		return 0
	
	# find first index violating descending order in reverse
	while end > 0 and nums[end] >= nums[end-1]:
		end -= 1
	
	# find min and max of our temporary window
	windowMax = max(nums[start:end+1])
	windowMin = min(nums[start:end+1])

	# extend the window
	while start > 0 and nums[start-1] > windowMin:
		start -= 1
            
	while end < n -1 and nums[end+1] < windowMax:
		end += 1

	return end - start + 1

