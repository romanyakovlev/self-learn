# first solution (dfs)

class Solution:
    def fill_land(self, i, j):
        if self.grid[i][j] == "1" and self.check_grid[i][j] == 0:
            self.check_grid[i][j] = 1
        else:
            return None
        if j - 1 >= 0:
            self.fill_land(i, j - 1)
        if j + 1 < len(self.grid[0]):
            self.fill_land(i, j + 1)
        if i - 1 >= 0:
            self.fill_land(i - 1, j)
        if i + 1 < len(self.grid):
            self.fill_land(i + 1, j)
    
    def find_island(self, i, j):
        while j < len(self.grid[0]):
            if self.grid[i][j] == "1" and self.check_grid[i][j] != 1:
                self.fill_land(i, j)
                self.counter += 1
                return True, (i, j)
            j += 1
        i += 1
        while i < len(self.grid):
            j = 0
            while j < len(self.grid[0]):
                if self.grid[i][j] == "1" and self.check_grid[i][j] != 1:
                    self.fill_land(i, j)
                    self.counter += 1
                    return True, (i, j)
                j += 1
            i += 1
        return False, (None, None)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.check_grid = [[0] * len(x) for x in grid]
        self.grid = grid
        self.counter = 0
        found = True
        ij = (0, 0)
        while found:
            found, ij = self.find_island(ij[0], ij[1])
        return self.counter


# solution from leetcode (using dfs - cool)

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
