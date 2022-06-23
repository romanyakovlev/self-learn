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

# using iteration - 1

class Solution:
                                
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while True:
            if left == right:
                return left if nums[left] == target else -1
            elif left > right:
                return -1
            index = (right + left) // 2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                right = index - 1
            else:
                left = index + 1
 
# using iteration - 2

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            index = (r + l) // 2
            if nums[index] > target:
                r = index - 1
            elif nums[index] < target:
                l = index + 1
            if nums[index] == target:
                return index
        return -1

# solution from disc

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = int(low + (high - low)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
