# first solution

class Solution:

    def sortColors(self, nums: List[int]) -> None:
        i = 0
        l, r = 0, len(nums) - 1
        while l <= i <= r:
            while True:
                if nums[i] == 0 and i > l:
                    nums[i], nums[l] = nums[l], nums[i]
                    l += 1
                elif nums[i] == 2 and i < r:
                    nums[i], nums[r] = nums[r], nums[i]
                    r -= 1
                else:
                    break
            i += 1
 
# solution from disc

# This is a dutch partitioning problem. We are classifying the array into four groups: red, white, unclassified, and blue. 
# Initially we group all elements into unclassified. We iterate from the beginning as long as the white pointer is less than the blue pointer.
# If the white pointer is red (nums[white] == 0), we swap with the red pointer and move both white and red pointer forward. 
# If the pointer is white (nums[white] == 1), the element is already in correct place, so we don't have to swap, just move the white pointer forward. 
# If the white pointer is blue, we swap with the latest unclassified element.

def sortColors(self, nums):
    red, white, blue = 0, 0, len(nums)-1
    
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
 
# same solution (rewritten)

class Solution:

    def sortColors(self, nums: List[int]) -> None:
        i = 0
        l, r = 0, len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1

