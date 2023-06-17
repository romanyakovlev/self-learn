
# first solution (slow)
class Solution:
    def fill_window(self, l, k):
        result = [l[0]]
        for i in range(1, k):
            j = 0
            while j < len(result):
                if result[j] < l[i]:
                    j += 1
                else:
                    result.insert(j, l[i])
                    break
            else:
                result.append(l[i])
        return result
    
    def find_median(self, w):
        i = len(w) // 2
        if len(w) % 2:
            return w[i]
        else:
            return (w[i] + w[i - 1]) / 2
    
    def modify_window(self, l, w, i, k):
        old_index = i - 1
        new_index = i + k - 1
        w.remove(l[old_index])
        j = 0
        while j < len(w):
            if w[j] < l[new_index]:
                j += 1
            else:
                w.insert(j, l[new_index])
                break
        else:
            w.append(l[new_index])
        return w
        
    
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        i = 0
        result = []
        w = None
        while i <= len(nums) - k:
            if w is not None:
                w = self.modify_window(nums, w, i, k)
            else:
                w = self.fill_window(nums, k)
            result.append(self.find_median(w))
            i += 1
        return result
            
            
# second solution - better approach (with binary search) - much faster

class Solution:

    def fill_window(self, l, k):
        result = [l[0]]
        for i in range(1, k):
            left, right = 0, len(result) - 1
            while left <= right:
                j = left + (right - left) // 2
                if result[j] < l[i]:
                    left = j + 1
                else:
                    right = j - 1
            if not result or result[-1] < l[i]:
                result.append(l[i])
            else:
                result.insert(j + (1 if result[j] < l[i] else 0), l[i])
        return result
    
    def find_median(self, w):
        i = len(w) // 2
        if len(w) % 2:
            return w[i]
        else:
            return (w[i] + w[i - 1]) / 2
    
    def modify_window(self, l, w, i, k):
        old_index = i - 1
        new_index = i + k - 1
        w.remove(l[old_index])
        left, right = 0, len(w) - 1
        while left <= right:
            j = left + (right - left) // 2
            if w[j] < l[new_index]:
                left = j + 1
            else:
                right = j - 1
        if not w or w[-1] < l[new_index]:
            w.append(l[new_index])
        else:
            w.insert(j + (1 if w[j] < l[new_index] else 0), l[new_index])
    
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        i = 1
        result = []
        limit = len(nums) - k
        w = self.fill_window(nums, k)
        result.append(self.find_median(w))
        while i <= limit:
            self.modify_window(nums, w, i, k)
            result.append(self.find_median(w))
            i += 1
        return result

# third solution - standard module use

class Solution:

    def fill_window(self, l, k):
        return sorted(l[:k])
    
    def find_median(self, w):
        i = len(w) // 2
        return w[i] if len(w) % 2 else (w[i] + w[i - 1]) / 2 
    
    def modify_window(self, l, w, i, k):
        old_index = i - 1
        new_index = old_index + k
        w.remove(l[old_index])
        bisect.insort(w, l[new_index])
    
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        i = 1
        result = []
        limit = len(nums) - k
        w = self.fill_window(nums, k)
        result.append(self.find_median(w))
        while i <= limit:
            self.modify_window(nums, w, i, k)
            result.append(self.find_median(w))
            i += 1
        return result

# 4th solution (using 2 heaps + hash table)

from heapq import *

class Solution:

    def pop_empty_left(self):
        while self.left_h and self.left_d[-self.left_h[0]] == 0:
            del self.left_d[-self.left_h[0]]
            heappop(self.left_h)
    
    def pop_empty_right(self):
        while self.right_h and self.right_d[self.right_h[0]] == 0:
            del self.right_d[self.right_h[0]]
            heappop(self.right_h)

    def push_to_left(self, val: int):
        if val not in self.left_d:
            self.left_d[val] = 1
            heappush(self.left_h, -val)
        else:
            self.left_d[val] += 1
        self.left_c += 1
    
    def push_to_right(self, val: int):
        if val not in self.right_d:
            self.right_d[val] = 1
            heappush(self.right_h, val)
        else:
            self.right_d[val] += 1
        self.right_c += 1

    def pop_from_left(self):
        val = -self.left_h[0]
        self.left_d[val] -= 1
        self.pop_empty_left()
        self.left_c -= 1
        return val

    def pop_from_right(self):
        val = self.right_h[0]
        self.right_d[val] -= 1
        self.pop_empty_right()
        self.right_c -= 1
        return val

    def add_element(self, val: int):
        if self.left_c == self.right_c:
            self.push_to_left(val)
            self.push_to_right(self.pop_from_left())
        else:
            self.push_to_right(val)
            self.push_to_left(self.pop_from_right())

    def get_median(self):
        if self.left_c == self.right_c:
            return (self.right_h[0] - self.left_h[0]) / 2
        else:
            return self.right_h[0]

    def remove_element(self, val: int):
        if val in self.left_d:
            self.left_d[val] -= 1
            self.pop_empty_left()
            self.left_c -= 1
        else:
            self.right_d[val] -= 1
            self.pop_empty_right()
            self.right_c -= 1
        if self.left_c - self.right_c == 1:
            self.push_to_right(self.pop_from_left())
        elif self.right_c - self.left_c == 2:
            self.push_to_left(self.pop_from_right())

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        self.left_d, self.right_d = dict(), dict()
        self.left_h, self.right_h = list(), list()
        self.left_c, self.right_c = 0, 0
        self.medians = []
        for i in range(k):
            self.add_element(nums[i])
        self.medians.append(self.get_median())
        for i in range(k, len(nums)):
            self.remove_element(nums[i - k])
            self.add_element(nums[i])
            self.medians.append(self.get_median())
        return self.medians

# solution from disc (2 heaps + lazy removal)

class Solution:
    # TC - O((n - k)*log(k))
    # SC - O(k)

    def find_median(self, max_heap, min_heap, heap_size):
        if heap_size % 2 == 1:
            return -max_heap[0]
        else:
            return (-max_heap[0] + min_heap[0]) / 2

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []
        min_heap = []
        heap_dict = defaultdict(int)
        result = []
        
        for i in range(k):
            heappush(max_heap, -nums[i])
            heappush(min_heap, -heappop(max_heap))
            if len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))
        
        median = self.find_median(max_heap, min_heap, k)
        result.append(median)
        
        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            heap_dict[prev_num] += 1

            balance = -1 if prev_num <= median else 1
            
            if nums[i] <= median:
                balance += 1
                heappush(max_heap, -nums[i])
            else:
                balance -= 1
                heappush(min_heap, nums[i])
            
            if balance < 0:
                heappush(max_heap, -heappop(min_heap))
            elif balance > 0:
                heappush(min_heap, -heappop(max_heap))

            while max_heap and heap_dict[-max_heap[0]] > 0:
                heap_dict[-max_heap[0]] -= 1
                heappop(max_heap)
            
            while min_heap and heap_dict[min_heap[0]] > 0:
                heap_dict[min_heap[0]] -= 1
                heappop(min_heap)

            median = self.find_median(max_heap, min_heap, k)
            result.append(median)
        
        return result
