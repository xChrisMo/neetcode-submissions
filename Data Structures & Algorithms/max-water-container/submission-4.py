class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amt = float('-inf')

        l = 0
        r = len(heights) - 1

        while l < r:
            cur_amt = min(heights[l], heights[r]) * (r - l)

            max_amt = max(max_amt, cur_amt)
            if heights[l] < heights[r]:
                l += 1

            else:
                r -= 1

        return max_amt