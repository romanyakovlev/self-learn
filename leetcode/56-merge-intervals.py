# first solution

class Solution:
    def merge_intervals(self, l):
        return [[min([x[0] for x in l]), max([x[1] for x in l])]]
    
    def merge_with_equal_intervals(self, l):
        if len(l) <= 1:
            return l
        result_l = [l[0]]
        for x in l[1:]:
            if result_l[-1][1] >= x[0]:
                result_l[-1] = [
                    min(result_l[-1][0], x[0]),
                    max(result_l[-1][1], x[1]),
                ]
            else:
                result_l.append(x)
        return result_l
    
    def check_list(self, l):
        i = 1
        while i < len(l):
            if l[i - 1][1] >= l[i][0]:
                return False
            i += 1
        return True
            
    def quick_sort(self, l):
        if len(l) <= 1:
            return l
        l1, l2, l3 = [], [], []
        i = len(l) // 2
        for x in range(len(l)):
            if l[x][0] < l[i][0] and l[x][1] < l[i][1]:
                l1.append(l[x])
            elif l[x][0] > l[i][0] and l[x][1] > l[i][1]:
                l2.append(l[x])
            else:
                l3.append(l[x])
        result = self.quick_sort(l1) + self.merge_intervals(l3) + self.quick_sort(l2)
        while not self.check_list(result):
            result = self.merge_with_equal_intervals(result)
        return result
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.quick_sort(intervals)
