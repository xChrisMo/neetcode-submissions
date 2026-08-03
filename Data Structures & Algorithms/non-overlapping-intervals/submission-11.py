class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # do a merge, return count - 1
    
        intervals.sort(key=lambda x:x[0])
        out = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < out[-1][1]:
                out[-1][1] = min(intervals[i][1], out[-1][1])

            else:
                out.append(intervals[i])

        return len(intervals) - len(out)