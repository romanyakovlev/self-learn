# first solution

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        index = 1
        last = nums[0]
        counter = 1
        while index < len(nums):
            if nums[index] != last:
                nums[counter] = nums[index]
                last = nums[counter]
                counter += 1
            index += 1
        return counter

# same but more elegant (disc)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums)-1):
        	if(nums[i]!=nums[i+1]):
        		nums[x] = nums[i+1]
        		x+=1
        return(x)

# or 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for x in range(len(nums) - 1):
            if nums[x+1] != nums[index]:
                index += 1
                nums[index] = nums[x+1]
        return index + 1
