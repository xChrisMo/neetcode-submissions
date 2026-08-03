class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
            # 1. Sort FIRST so the logic applies to the correct order
        intervals.sort(key=lambda x: x[0])
        
        out = [intervals[0]]
        
        for i in range(1, len(intervals)):
            # Overlap detected
            if intervals[i][0] < out[-1][1]:
                # GREEDY FIX: Keep the interval that ends earlier.
                # We don't append anything to 'out', we just update the 
                # end time of the current "active" interval to the minimum.
                out[-1][1] = min(out[-1][1], intervals[i][1])
            else:
                # No overlap, safe to add to our non-overlapping set
                out.append(intervals[i])

        # Total intervals minus the ones we successfully kept
        return len(intervals) - len(out)