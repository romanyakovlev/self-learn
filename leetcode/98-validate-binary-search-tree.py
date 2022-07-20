
# first solution

class Solution:
    def check_values(self, root, value, direction):
        print(root.val, value, direction)
        if direction == "right" and root.val <= value:
            return False
        elif direction == "left" and root.val >= value:
            return False
        if root.left and root.right:
            return (
                self.check_values(root.left, value, direction) and 
                self.check_values(root.right, value, direction)
            )
        elif root.left:
            return self.check_values(root.left, value, direction)
        elif root.right:
            return self.check_values(root.right, value, direction)
        else:
            return True
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left and root.right:
            return (
                self.check_values(root.left, root.val, "left") and 
                self.check_values(root.right, root.val, "right") and
                self.isValidBST(root.left) if root.val > root.left.val else False and
                self.isValidBST(root.right) if root.val < root.right.val else False
            )
        elif root.left:
            return (
                self.check_values(root.left, root.val, "left") and
                self.isValidBST(root.left) if root.val > root.left.val else False
            )
        elif root.right:
            return (
                self.check_values(root.right, root.val, "right") and
                self.isValidBST(root.right) if root.val < root.right.val else False
            )
        else:
            return True

