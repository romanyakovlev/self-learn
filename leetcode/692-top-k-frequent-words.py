
# first solution

import heapq
class Solution:
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d_c, d_w = {}, {}
        h, r = [], []
        c = 0
        for w in words:
            d_c[w] = d_c.get(w, 0) + 1
        for w, w_c in d_c.items():
            d_w[w_c] = d_w.get(w_c, []) + [w]
        for w_c, w_l in d_w.items():
            heapq.heappush(h, (-w_c, w_l))
        while True:
            for w in sorted(heapq.heappop(h)[1]):
                r.append(w)
                c += 1
                if c == k:
                    return r
