from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i, (x, y) in enumerate(points):
            r = (x ** 2 + y ** 2) ** 0.5
            heappush(h, (r, i))
        indexes = []
        for _ in range(k):
            indexes.append(heappop(h)[1])
        return [points[i] for i in indexes]
