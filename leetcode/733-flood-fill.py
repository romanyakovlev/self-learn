class Solution:
    def recurse(self, x, y):
        self.image_set.add((x, y))
        if self.origin_color == self.image[x][y]:
            self.image[x][y] = self.new_color
            if x - 1 >= 0 and (x - 1, y) not in self.image_set:
                self.recurse(x - 1, y)
            if x + 1 <= self.x_limit and (x + 1, y) not in self.image_set:
                self.recurse(x + 1, y)
            if y - 1 >= 0 and (x, y - 1) not in self.image_set:
                self.recurse(x, y - 1)
            if y + 1 <= self.y_limit and (x, y + 1) not in self.image_set:
                self.recurse(x, y + 1)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.origin_color = image[sr][sc]
        self.new_color = newColor
        self.x_limit = len(image) - 1
        self.y_limit = len(image[0]) - 1
        self.image_set = set()
        self.recurse(sr, sc)
        return self.image
        
