# solution

from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.left and -self.left[0] < num:
            heappush(self.right, num)
        else:
            heappush(self.left, -num)
        if len(self.left) - len(self.right) == 2:
            heappush(self.right, -heappop(self.left))
        elif len(self.right) - len(self.left) == 2:
            heappush(self.left, -heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.left) < len(self.right):
            return self.right[0]
        elif self.left and self.right:
            return (-self.left[0] + self.right[0]) / 2 
        return 0

# disc solution

from heapq import *

class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
