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
        
# iterative approach

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        l = []
        temp = []
        while root:
            l.append(root.val)
            if root.children:
                temp.extend(root.children[::-1])
            root = temp.pop() if temp else None
        return l
        
