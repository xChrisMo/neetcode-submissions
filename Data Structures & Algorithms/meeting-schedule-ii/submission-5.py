from heapq import heappush, heappop
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
       
        # start_arr = [0, 5, 10]
        # end_arr = [40, 10, 20]

        # so I can loop through using each end, to see if it is > start, if it is, I count + 1

        start_arr = [i.start for i in intervals]
        end_arr = [i.end for i in intervals]

        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heappop(min_heap)
            heappush(min_heap, interval.end)

        return len(min_heap)