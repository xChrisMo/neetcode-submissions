class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # do a merge, return res - 1
        
        intervals.sort(key=lambda x:x[0])
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prevEnd:
                res += 1
                prevEnd = min(end, prevEnd)

            else:
                prevEnd = end

        return res