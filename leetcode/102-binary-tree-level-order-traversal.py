# using recursion

class Solution:
    def recurse(self, root, i):
        if root is None:
            return
        if len(self.l) < i:
            self.l.append([])
        self.l[i - 1].append(root.val)
        self.recurse(root.left, i + 1)
        self.recurse(root.right, i + 1)
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.l = []
        self.recurse(root, 1)
        return self.l
        
