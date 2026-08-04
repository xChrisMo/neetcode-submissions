class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        out = []

        for q in queries:
            min_l = float('inf')
            for start, end in intervals:
                if start <= q <= end:
                    min_l = min(min_l, end - start + 1)

            if min_l == float('inf'):
                out.append(-1)
            else:
                out.append(min_l)

        return out