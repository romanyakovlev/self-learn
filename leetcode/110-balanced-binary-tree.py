# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def get_depth(self, root, c):
        if root and root.left and root.right:
            left = self.get_depth(root.left, c + 1)
            right = self.get_depth(root.right, c + 1)
            return left if left >= right else right
        elif root and root.left:
            return self.get_depth(root.left, c + 1)
        elif root and root.right:
            return self.get_depth(root.right, c + 1)
        else:
            return c
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root and root.left and root.right:
            return (
                self.isBalanced(root.left) and 
                self.isBalanced(root.right) and 
                abs(self.get_depth(root.left, 1) - self.get_depth(root.right, 1)) <= 1
            )
        elif root and root.left:
            return self.isBalanced(root.left) and self.get_depth(root.left, 1) <= 1
        elif root and root.right:
            return self.isBalanced(root.right) and self.get_depth(root.right, 1) <= 1
        else:
            return True
