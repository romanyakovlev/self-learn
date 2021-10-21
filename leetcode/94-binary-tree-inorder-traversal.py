# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def go_to_root(self, root):
        if root.left:
            self.go_to_root(root.left)
        if root.val:
            self.nodes.append(root.val)
        if root.right:
            self.go_to_root(root.right)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.nodes = []
        if root:
            self.go_to_root(root)
        return self.nodes
        
# solitions from desc
# all DFS (depth first search)

def preorder(root):
  return [root.val] + preorder(root.left) + preorder(root.right) if root else []
def inorder(root):
  return  inorder(root.left) + [root.val] + inorder(root.right) if root else []
def postorder(root):
  return  postorder(root.left) + postorder(root.right) + [root.val] if root else []

# other 

# recursively
def inorderTraversal1(self, root):
    res = []
    self.helper(root, res)
    return res
    
def helper(self, root, res):
    if root:
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
 
# iteratively       
def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
