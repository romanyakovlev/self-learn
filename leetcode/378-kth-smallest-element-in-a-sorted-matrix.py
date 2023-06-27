# 1st (using k-way merge)

from heapq import *

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        c = 0
        for r in matrix:
            heappush(h, (r[0], r, 0))
        while c != k:
            v, r, i = heappop(h)
            c, i = c + 1, i + 1
            if len(r) > i:
                heappush(h, (r[i], r, i))
        return v
