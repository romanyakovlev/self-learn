from heapq import heappush, heappop


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort(key=lambda x: (x[0], x[1]), reverse=True)
        h = []
        c = 1
        while A:
            m = A.pop()
            while h:
                x = (h[0][1], h[0][0])
                if x[1] <= m[0]:
                    heappop(h)
                else:
                    break
            heappush(h, (m[1], m[0]))
            c = max(c, len(h))
        return c
