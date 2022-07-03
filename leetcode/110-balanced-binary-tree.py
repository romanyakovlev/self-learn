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

# solutions from leetcode

# recursive (same as my but more elegant)
class Solution(object):
    def isBalanced(self, root):
            
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1
    
# Iterative, based on postorder traversal
class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True
