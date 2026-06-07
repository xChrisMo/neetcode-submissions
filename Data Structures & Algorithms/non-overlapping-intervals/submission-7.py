class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        res = 0
        prev_end = intervals[0][1]

        #[[1,2],[1,4],[2,4]]

        for start, end in intervals[1:]:
            if prev_end > start:
                res += 1
                prev_end = min(end, prev_end)

            else:
                prev_end = end

        return res
