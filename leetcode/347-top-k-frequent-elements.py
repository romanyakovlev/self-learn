
# first solution

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        h, l = [], []
        for n in nums:
            d[n] = d.get(n, 0) + 1
        for n, c in d.items():
            heapq.heappush(h, (-c, n))
        return [heapq.heappop(h)[1] for _ in range(k)]
