

# first solution 
# 1. use heap (heapq module) - finds max value in window
# 2. use hash map - check if value in window or not
# 3. the trick is to check that max value from heap in hash map. 
# if yes, return max from heap. if no, pop max from heap and repeat 
# it step until we find value which is inside hash map
import heapq
class Solution:
    
    def fill_window(self, l, k):
        w = []
        d = {}
        for x in l[:k]:
            heapq.heappush(w, -x)
            d[x] = d.get(x, 0) + 1
        return w, d
    
    def get_max(self, h, d):
        while True:
            if -h[0] in d.keys():
                return -h[0]
            else:
                heapq.heappop(h)
    
    def modify_window(self, l, h, d, k, i):
        old_index = i - 1
        new_index = old_index + k
        d[l[old_index]] -= 1
        if d[l[old_index]] == 0:
            del d[l[old_index]]
        heapq.heappush(h, -l[new_index])
        d[l[new_index]] = d.get(l[new_index], 0) + 1
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 1
        r = []
        h, d = self.fill_window(nums, k)
        r.append(self.get_max(h, d))
        limit = len(nums) - k
        while i <= limit:
            self.modify_window(nums, h, d, k, i)
            r.append(self.get_max(h, d))
            i += 1
        return r
