

class Solution:
    def get_index(self, l):
        return len(l) // 2
    
    def recurse(self, l):
        i = self.get_index(l)
        if not l:
            return None
        else:
            node = TreeNode(l[i])
            node.left = self.recurse(l[:i])
            node.right = self.recurse(l[i+1:])
            return node
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        i = self.get_index(nums)
        self.node = TreeNode(nums[i])
        self.node.left = self.recurse(nums[:i])
        self.node.right = self.recurse(nums[i+1:])
        return self.node
        
# better solution (withoug using slicing)

# A lot of the Python solutions use slices to split the array; 
# however, it takes O(n) to slice, making the entire algorithm O(n logn). 
# Therefore, we create a helper function to pass in the bounds of the array instead, making it O(n):

def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
	return self.helper(nums, 0, len(nums))

def helper(self, nums, lower, upper):
	if lower == upper:
		return None

	mid = (lower + upper) // 2
	node = TreeNode(nums[mid])
	node.left = self.helper(nums, lower, mid)
	node.right = self.helper(nums, mid+1, upper)

	return node

# Please note the if lower == upper: return None statement -- since we are passing in bounds, 
# nums will never be None. Therefore, we check if the lower and upper bounds are the same for our base case.
            
