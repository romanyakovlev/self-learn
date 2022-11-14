# 1st

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = intervals + [newInterval]
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for interval in intervals[1:]:
            if result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result

# 2nd

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:        
        for i in range(len(intervals)):
            # 1. do not overlap, newInterval before intervals
            if intervals[i][0] > newInterval[1]:
                intervals.insert(0, newInterval)
            # 2. do overlap
            elif intervals[i][0] >= newInterval[0] or intervals[i][1] >= newInterval[0]:
                j = i
                while j + 1 < len(intervals) and intervals[j + 1][0] <= newInterval[1]:
                    j += 1
                intervals[i][0], intervals[i][1] = min(intervals[i][0], newInterval[0]), max(intervals[j][1], newInterval[1])
                del intervals[i + 1:j + 1]
            # 3. do not overlap, newInterval inside intervals
            elif i + 1 < len(intervals) and intervals[i][1] < newInterval[0] and newInterval[1] < intervals[i + 1][0]:
                intervals.insert(i + 1, newInterval)
            else:
                continue
            break
        else:
            # 4. do not overlap, newInterval after intervals
            intervals.append(newInterval)
        return intervals

