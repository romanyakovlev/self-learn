# 1st (2 heaps pattern)

from heapq import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.l, self.r = [], []
        h = nums
        heapify(h)
        for _ in range(len(h) - k):
            heappush(self.l, -heappop(h))
        for _ in range(len(h)):
            heappush(self.r, heappop(h))

    def add(self, val: int) -> int:
        if len(self.r) < self.k:
            heappush(self.r, val)
            return self.r[0]
        if self.r[0] < val:
            heappush(self.l, -heappushpop(self.r, val))
        else:
            heappush(self.l, -val)
        return self.r[0]
