# first solution 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not len(nums):
            return 0
        l_index = 0
        r_index = len(nums) - 1
        while (r_index - l_index) > 0:
            if nums[r_index] == val:
                r_index -= 1
                continue
            if nums[l_index] == val:
                nums[l_index], nums[r_index] = nums[r_index], nums[l_index]
            l_index += 1
        return l_index + 1 if nums[l_index] != val else l_index


# more elegant way (disc)

class Solution:
  def removeElement(self, nums, val):
    start, end = 0, len(nums) - 1
    while start <= end:
        if nums[start] == val:
            nums[start], nums[end], end = nums[end], nums[start], end - 1
        else:
            start +=1
    return start
