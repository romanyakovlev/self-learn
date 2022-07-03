# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first solution

class Solution:
    def recurse(self, root: Optional[TreeNode], l: list, s: str):
        if root:
            s += root.val
            l += [root.val]
            if s == self.target and not root.left and not root.right:
                self.result_l.append(l)
                return None
            if root.left:
                self.recurse(root.left, l[:], s)
            if root.right:
                self.recurse(root.right, l[:], s)
            
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        s = 0
        l = []
        self.result_l = []
        self.target = targetSum
        self.recurse(root, l[:], s)
        return self.result_l
        
