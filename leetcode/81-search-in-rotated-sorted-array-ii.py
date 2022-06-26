# first solution

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            i = l + (r - l) // 2
            if nums[i] == target:
                return True
            elif nums[l] == nums[r]:
                if nums[l] == target:
                    return True
                r -= 1
                l += 1
            elif nums[i] > target:
                if nums[i] > nums[r] and target < nums[l]:
                    l = i + 1
                else:
                    r = i - 1
            else:
                if nums[i] < nums[l] and target > nums[r]:
                    r = i - 1
                else:
                    l = i + 1
        return False

# solution from leetcode

"""
Since the array is given in a sorted order, so it can be solved using the binary search algorithm.

To solve this problem we have to follow the folllowing steps:

1. Calculate the mid index.
2. Check if the mid element == target, return True else move to next step.
3. Else if the mid element >= left.
if mid element >= target and and left <= target, then shift right to mid-1 position, else shift left to mid+1 position.
4. Else,
If target >= mid element and target <=right, then shift left to mid+1 position, else shift right to mid-1 position.
5. If the element is not found return False
Note: Since duplicate elemnts are present in the array so remove all the duplicates before step step 1.
To remove duplicate,

Shift left while left == left+1, and
Shift right while right == right-1.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        # If the length of the given array list is 1, then check the first element and return accordingly
        if len(nums)==1:
            if nums[0]!=target:
                return False
            else:
                return True
        left=0
        right=len(nums)-1
        # binary search 
        while(left<=right):
            # shifting to remove duplicate elements
            while left<right and nums[left] == nums[left+1]:
                left+=1
            while left<right and nums[right] == nums[right-1]:
                right-=1
            # step 1 calculate the mid    
            mid=(left+right)//2
            #step 2
            if nums[mid]==target:
                return True
            #step 3
            elif nums[left]<=nums[mid]:
                if nums[mid]>=target and nums[left]<=target:
                    right=mid-1
                else:
                    left=mid+1
            # step 4
            else:
                if target>=nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        # step 5
        return False
