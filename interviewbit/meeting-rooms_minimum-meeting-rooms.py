from heapq import heappush, heappop


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort(key=lambda x: (x[0], x[1]), reverse=True)
        heap = []
        counter = 1
        while A:
            room = A.pop()
            while heap:
                # swap end and start again (from string #20)
                room_with_min_end_from_heap = (heap[0][1], heap[0][0])
                if room_with_min_end_from_heap[1] <= room[0]:
                    heappop(heap)
                else:
                    break
            # swap end and start to build heap properly
            heappush(heap, (room[1], room[0]))
            counter = max(counter, len(heap))
        return counter
