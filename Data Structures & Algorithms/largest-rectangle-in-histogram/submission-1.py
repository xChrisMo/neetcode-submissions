class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # []

        # n = len(heights)
        # add index and height to stack
        # while stack and stack[-1][1] > height:
        # j, old_h = stack.pop()
        # max_area = max(max_area, (i - j) * old_h)
        # i = min(i, j)
        # add it to stack

        # while stack:
        # i, hieght = stack.pop()
        # max_area = max(max_area, (n - i) * height)
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                j, old_h = stack.pop()
                max_area = max(max_area, (i - j) * old_h)
                start = j

            stack.append([start, height])

        while stack:
            i, height = stack.pop()
            max_area = max(max_area, (len(heights) - i) * height)

        return max_area


    # [2, 1, 5, 6, 2, 3]

    # [[0, 1], [2, 5], [2, 2], []]
