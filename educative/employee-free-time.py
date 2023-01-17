

from __future__ import print_function
import heapq

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

    def __lt__(self, other):
        return self.start < other.start


def find_employee_free_time(schedule):
    h = []
    for i in range(len(schedule)):
        heapq.heappush(h, (schedule[i][0], 1, i))
    m_l = []  # merged intervals list
    while h:
        interval, interval_i, schedule_i = heapq.heappop(h)
        if interval_i < len(schedule[schedule_i]):
            heapq.heappush(h, (schedule[schedule_i][interval_i], interval_i + 1, schedule_i))
        if m_l and m_l[-1].end >= interval.start:
            m_l[-1].end = max(m_l[-1].end, interval.end)
        else:
            m_l.append(interval)
    if len(m_l) == 1:
        return []
    r = []
    for i in range(1, len(m_l)):
        r.append(Interval(start=m_l[i - 1].end, end=m_l[i].start))
    return r


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
