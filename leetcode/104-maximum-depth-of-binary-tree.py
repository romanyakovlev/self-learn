class Solution:
    def recurse(self, node, depth):
        if depth > self.max_depth:
            self.max_depth = depth
        if node.left:
            self.recurse(node.left, depth + 1)
        if node.right:
            self.recurse(node.right, depth + 1)
           
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        if not root:
            return 0
        self.recurse(root, 1)
        return self.max_depth


# BFS solution
# At every level, "queue" ends up being a list of all the nodes 
# at that level. We increase the depth till the time "queue" is an empty list.

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
            
        return depth
