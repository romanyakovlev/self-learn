# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_recursive(self, p, q):
        if self.same:
            if p.val != q.val:
                self.same = False
                return None
            if p.left and q.right:
                self.check_recursive(p.left, q.right)
            elif (p.left and not q.right) or (not p.left and q.right):
                self.same = False
                return None
            if p.right and q.left:
                self.check_recursive(p.right, q.left)
            elif (p.right and not q.left) or (not p.right and q.left):
                self.same = False
                return None

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.same = True
        p, q = root.left, root.right
        if p and q:
            self.check_recursive(p, q) 
        elif p != q:
            self.same = False
        return self.same

# second solution

class Solution:

    def recurse(self, left:  Optional[TreeNode], right:  Optional[TreeNode]) -> bool:
        if left and right:
            return (
                self.recurse(left.left, right.right) and 
                self.recurse(left.right, right.left) and
                left.val == right.val
            )
        elif (not left and right) or (left and not right):
            return False
        else:
            return True
            
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.recurse(root.left, root.right)
