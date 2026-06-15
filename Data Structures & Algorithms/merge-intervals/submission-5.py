class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = [intervals[0]]

        for interval in intervals[1:]:
            if out[-1][1] >= interval[0]:
                out[-1][0] = min(out[-1][0], interval[0])
                out[-1][1] = max(out[-1][1], interval[1])
            else:
                out.append(interval)

        return out