# recursive approach

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        l = []
        if root:
            l.append(root.val)
            if root.children:
                for c in root.children:
                    l.extend(self.preorder(c))
        return l
        
