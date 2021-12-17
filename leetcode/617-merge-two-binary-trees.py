# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, r, r1, r2):
        if r1 or r2:
            r.val = (r1.val if r1 else 0) + (r2.val if r2 else 0)
        if (r1 and r1.left) or (r2 and r2.left):
            r.left  = TreeNode()
            self.recurse(r.left, r1.left if r1 else None, r2.left if r2 else None)
        if (r1 and r1.right) or (r2 and r2.right):
            r.right  = TreeNode()
            self.recurse(r.right, r1.right if r1 else None, r2.right if r2 else None)
    
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 or root2:
            root = TreeNode()
        else:
            return None
        self.recurse(root, root1, root2)
        return root
