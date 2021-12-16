# first slow solution

class Solution:
    def recurse(self, x, y, grid_set, root=False):
        if (x, y) in self.checked and not root:
            return 0
        c = 0
        grid_set.add((x, y))
        if self.grid[x][y] == 1:
            c += 1
            if x - 1 >= 0 and (x - 1, y) not in grid_set:
                c += self.recurse(x - 1, y, grid_set)
            if x + 1 <= self.x_limit and (x + 1, y) not in grid_set:
                c += self.recurse(x + 1, y, grid_set)
            if y - 1 >= 0 and (x, y - 1) not in grid_set:
                c += self.recurse(x, y - 1, grid_set)
            if y + 1 <= self.y_limit and (x, y + 1) not in grid_set:
                c += self.recurse(x, y + 1, grid_set)
        return c
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        max_c = 0
        self.x_limit = len(grid) - 1
        self.y_limit = len(grid[0]) - 1
        self.checked = set()
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                self.checked.add((x, y))
                grid_set = set()
                c = self.recurse(x, y, grid_set, root=True)
                max_c = max(max_c, c)
        return max_c

# same but with results caching (alot better perfmonace)
class Solution:
    def recurse(self, x, y, grid_set):
        if (x, y) in self.cached.keys():
            return self.cached[(x, y)]
        c = 0
        grid_set.add((x, y))
        if self.grid[x][y] == 1:
            c += 1
            if x - 1 >= 0 and (x - 1, y) not in grid_set:
                c += self.recurse(x - 1, y, grid_set)
            if x + 1 <= self.x_limit and (x + 1, y) not in grid_set:
                c += self.recurse(x + 1, y, grid_set)
            if y - 1 >= 0 and (x, y - 1) not in grid_set:
                c += self.recurse(x, y - 1, grid_set)
            if y + 1 <= self.y_limit and (x, y + 1) not in grid_set:
                c += self.recurse(x, y + 1, grid_set)
        self.cached[(x, y)] = c
        return c
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        max_c = 0
        self.x_limit = len(grid) - 1
        self.y_limit = len(grid[0]) - 1
        self.cached = dict()
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                grid_set = set()
                c = self.recurse(x, y, grid_set)
                max_c = max(max_c, c)
        return max_c
        
        
