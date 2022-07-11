# first solution

class Solution:
    def fill_land(self, grid, i, j):
        if grid[i][j] == "1" and self.check_grid[i][j] == 0:
            self.check_grid[i][j] = 1
        else:
            return None
        if j - 1 >= 0:
            self.fill_land(grid, i, j - 1)
        if j + 1 < len(grid[0]):
            self.fill_land(grid, i, j + 1)
        if i - 1 >= 0:
            self.fill_land(grid, i - 1, j)
        if i + 1 < len(grid):
            self.fill_land(grid, i + 1, j)
    
    def find_island(self, grid, i, j):
        while j < len(grid[0]):
            if grid[i][j] == "1" and self.check_grid[i][j] != 1:
                self.fill_land(grid, i, j)
                self.counter += 1
                return True, (i, j)
            j += 1
        i += 1
        while i < len(grid):
            j = 0
            while j < len(grid[0]):
                if grid[i][j] == "1" and self.check_grid[i][j] != 1:
                    self.fill_land(grid, i, j)
                    self.counter += 1
                    return True, (i, j)
                j += 1
            i += 1
        return False, (None, None)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.check_grid = [[0] * len(x) for x in grid]
        self.counter = 0
        ij = (None, None)
        while True:
            found, ij = self.find_island(
                grid, 
                ij[0] if ij[0] is not None else 0,
                ij[1] if ij[1] is not None else 0,
            )
            if not found:
                break
        return self.counter
