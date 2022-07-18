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
        
# using iteration

class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = []
        level_list = []
        if root:
            level_list.append(root)
        while level_list:
            temp_val = []
            temp_list = []
            for e in level_list:
                # create level list with values - temp_val
                temp_val.append(e.val)
                # create next level - temp_list
                if e.left:
                    temp_list.append(e.left)
                if e.right:
                    temp_list.append(e.right)
            l.append(temp_val)
            level_list = temp_list
        return l

# solution from disc - same as my

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result: List[List[int]] = []
        lay = [root]
        while lay:
            lay_values = []
            next_lay = []
            
            for node in lay:
                lay_values.append(node.val)
                if node.left:
                    next_lay.append(node.left)
                if node.right:
                    next_lay.append(node.right)
            
            lay = next_lay
            result.append(lay_values)
        
        return result
