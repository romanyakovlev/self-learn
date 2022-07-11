# first solution

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
