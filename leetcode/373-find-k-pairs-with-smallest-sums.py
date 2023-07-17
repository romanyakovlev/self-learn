# 1st solution

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h, l = [], []
        heappush(h, (nums1[0], nums1, 0))
        heappush(h, (nums2[0], nums2, 0))
        while len(h) == 2:
            v, n, i = heappop(h)
            inserted = False
            v2, n2, i2 = h[0]
            while i2 < len(n2) and not (len(l) == k and -l[0][0] < v + n2[i2]):
                heappush(l, (-(v + n2[i2]), [v, n2[i2]] if n is nums1 else [n2[i2], v]))
                if len(l) > k:
                    heappop(l)
                inserted = True
                i2 += 1
            i += 1
            if i < len(n) and inserted:
                heappush(h, (n[i], n, i))
        l = [heappop(l)[1] for _ in range(len(l))]
        return list(reversed(l))
