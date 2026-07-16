class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # for every index, run another loop, 
        # use the minimum * distance to comepare maxh

        max_water = 0
        n = len(heights)

        for i in range(n):
            for j in range(i + 1, n):
                max_water = max(max_water, min(heights[i], heights[j]) * (j - i))


        return max_water