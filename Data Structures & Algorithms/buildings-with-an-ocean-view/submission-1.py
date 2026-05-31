class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # n = len(heights)
        # highest = float('-inf')
        # out = []

        # for i in range(n-1, -1, -1):
        #     if heights[i] > highest:
        #         highest = heights[i]
        #         out.append(i)


        # return sorted(out)

        stack = []

        for index, height in enumerate(heights):
            while stack and height >= heights[stack[-1]]:
                stack.pop()

            stack.append(index)

        return stack