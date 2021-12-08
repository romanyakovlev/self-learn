# solution using recursion

class Solution:
    def recurse(self, index, new_value, counter):
        old_value = self.nums[index]
        self.nums[index] = new_value
        if counter != 0:
            if index in self.already_seen:
                self.recurse(
                    (index + self.k + 1) % len(self.nums), 
                    self.nums[index + 1], 
                    counter
                )
            else:
                self.already_seen.add(index)
                self.recurse(
                    (index + self.k) % len(self.nums), 
                    old_value, 
                    counter - 1
                )
        
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.already_seen = set()
        self.k = k
        self.nums = nums
        index = k % len(self.nums)
        self.recurse(index, nums[0], len(self.nums) - 1)
        return self.nums

# using iteration

class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        already_seen = set()
        index = k % len(nums)
        index, new_value, counter = index, nums[0], len(nums) - 1
        while counter >= 0:
            old_value = nums[index]
            nums[index] = new_value
            if index in already_seen:
                index, new_value, counter = (index + k + 1) % len(nums), nums[index + 1], counter
            else:
                already_seen.add(index)
                index, new_value, counter = (index + k) % len(nums), old_value, counter - 1
