# using recursion

class Solution:
    
    def get_index(self, l, r):
        return (r + l) // 2
        
    def recurse(self, left, right, nums, target):
        if left == right:
            return left if nums[left] == target else -1
        elif left > right:
            return -1
        index = self.get_index(left, right)
        if nums[index] == target:
            return index
        elif nums[index] > target:
            return self.recurse(left, index - 1, nums, target)
        else:
            return self.recurse(index + 1, right, nums, target)
                                
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        return self.recurse(left, right, nums, target)

# using iteration
#...
