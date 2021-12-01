

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
        

            
