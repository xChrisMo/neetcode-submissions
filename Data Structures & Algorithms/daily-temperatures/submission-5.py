class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # for loop from 0 to n - 1

        # [(30, 0), 38]
        # [0, 0, 0, 0, 0, 0, 0]
        n = len(temperatures)
        out = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                # so the current index now that is greater than prev - prev index!
                tmp, j = stack.pop()
                out[j] = i - j
            stack.append((temp, i))

        return out