# first approach

from queue import Queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        x_limit = len(grid) - 1
        y_limit = len(grid[0]) - 1
        q = Queue()
        max_index = 0
        not_rotten = set()
        for x in range(x_limit + 1):
            for y in range(y_limit + 1):
                if grid[x][y] == 2:
                    index, grid_set = 0, set()
                    q.put((index, (x, y), grid_set))
                elif grid[x][y] == 1:
                    not_rotten.add((x, y))
        while not q.empty():
            index, (x, y), grid_set = q.get()
            grid_set.add((x, y))
            if grid[x][y] != 0:
                if grid[x][y] == 1:
                    grid[x][y] = 2
                    index += 1
                    not_rotten.remove((x, y))
                max_index = max(max_index, index)
                if x - 1 >= 0 and (x - 1, y) not in grid_set and grid[x - 1][y] == 1:
                    q.put((index,  (x - 1, y), grid_set))
                if x + 1 <= x_limit and (x + 1, y) not in grid_set and grid[x + 1][y] == 1:
                    q.put((index,  (x + 1, y), grid_set))
                if y - 1 >= 0 and (x, y - 1) not in grid_set and grid[x][y - 1] == 1:
                    q.put((index,  (x, y - 1), grid_set))
                if y + 1 <= y_limit and (x, y + 1) not in grid_set and grid[x][y + 1] == 1:
                    q.put((index,  (x, y + 1), grid_set))
        return - 1 if not_rotten else max_index
        
        
        
        
