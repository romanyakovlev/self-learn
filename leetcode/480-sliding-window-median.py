
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
            
            
# better approach (with binary search)

class Solution:

    def fill_window(self, l, k):
        result = [l[0]]
        for i in range(1, k):
            left, right = 0, len(result) - 1
            j = 0
            while left <= right:
                j = (left + right) // 2
                if result[j] < l[i]:
                    left = j + 1
                else:
                    right = j - 1
            if (j == len(result) - 1 and result[-1] < l[i]) or not result:
                result.append(l[i])
            elif result[j] < l[i]:
                result.insert(j + 1, l[i])
            else:
                result.insert(j, l[i])
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
        j = 0
        while left <= right:
            j = (left + right) // 2
            #print(j, left, right)
            if w[j] < l[new_index]:
                left = j + 1
            else:
                right = j - 1
        if (j == len(w) - 1 and w[-1] < l[new_index]) or not w:
            w.append(l[new_index])
        elif w[j] < l[new_index]:
            w.insert(j + 1, l[new_index])
        else:
            w.insert(j, l[new_index])
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
