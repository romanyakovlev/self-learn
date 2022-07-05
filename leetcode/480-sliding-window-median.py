
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
        if len(w) % 2:
            return w[i]
        else:
            return (w[i] + w[i - 1]) / 2
    
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

