# first solution

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l<=r:
            i = l + (r - l) // 2
            # check if arr is rotated and min val is located on the left side from i element - move left side
            # '+ 1' here is because nums[i] element is 100% greater than left value ([..5,1,2,3]) 
            # so chose next item  - nums[i + 1]
            if nums[l] <= nums[i] >= nums[r]:
                l = i + 1
            # check if arr is rotated and min val is located on the right side from i element - move right side
            elif nums[l] >= nums[i] <= nums[r]:
                r = i
            # check if arr is not rotated - it is reversed - mode left side 
            elif nums[l] >= nums[i] >= nums[r]:
                l = i
            # check if arr is not rotated - it is not reversed - mode right side 
            elif nums[l] <= nums[i] <= nums[r]:
                r = i
        return nums[i]

# solution from leetcode discussion (really beautiful)

class Solution:
    def findMin(self, num):
        first, last = 0, len(num) - 1
        while first < last:
            midpoint = (first + last) // 2
            if num[midpoint] > num[last]:
                first = midpoint + 1
            else:
                last = midpoint
        return num[first]
