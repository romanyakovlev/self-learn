# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_recursive(self, p, q):
        if self.same:
            if p.left and q.left:
                self.check_recursive(p.left, q.left)
            elif (p.left and not q.left) or (not p.left and q.left):
                self.same = False
            if p.val != q.val:
                self.same = False
            if p.right and q.right:
                self.check_recursive(p.right, q.right)
            elif (p.right and not q.right) or (not p.right and q.right):
                self.same = False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True
        if p and q:
            self.check_recursive(p, q) 
        elif p != q:
            self.same = False
        return self.same
    
# second solution
class Solution:
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return p.val == q.val and left and right
        elif (not q and p) or (q and not p):
            return False
        else:
            return True
