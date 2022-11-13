# first solution
# use sorting with intervals merging
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
            
    def sort_intervals(self, l):
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
        result = self.sort_intervals(l1) + self.merge_intervals(l3) + self.sort_intervals(l2)
        while not self.check_list(result):
            result = self.merge_with_equal_intervals(result)
        return result
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.sort_intervals(intervals)

    
# second - solution with internal functions (much faster)

class Solution:
    
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
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = sorted(intervals, key=lambda x: x[0])
        while not self.check_list(result):
            result = self.merge_with_equal_intervals(result)
        return result


# 3rd solution

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0], x[1]))
        result = [intervals[0]]
        for interval in intervals[1:]:
            if result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result

