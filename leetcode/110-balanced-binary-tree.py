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
            return max(left, right)
        elif root and root.left:
            return self.get_depth(root.left, c + 1)
        elif root and root.right:
            return self.get_depth(root.right, c + 1)
        else:
            return c
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root and root.left and root.right:
            left_val = self.get_depth(root.left, 1)
            right_val = self.get_depth(root.right, 1)
            left = self.isBalanced(root.left)
            right = self.isBalanced(root.right)
            return left and right and abs(left_val - right_val) <= 1
        elif root and root.left:
            left_val = self.get_depth(root.left, 1)
            left = self.isBalanced(root.left)
            return left and left_val <= 1
        elif root and root.right:
            right_val = self.get_depth(root.right, 1)
            right = self.isBalanced(root.right)
            return right and right_val <= 1
        else:
            return True
        
