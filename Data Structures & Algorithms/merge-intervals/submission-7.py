class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])
        output = [intervals[0]]

        for i in intervals:
            latest = output[-1]

            if i[0] > latest[1]:
                output.append(i)
            else:
                latest[0] = min(latest[0], i[0])
                latest[1] = max(latest[1], i[1])
        
        return output