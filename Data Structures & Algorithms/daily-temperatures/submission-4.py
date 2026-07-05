class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                # we need to find the next one that 
                cur_temp, cur_ind = stack.pop()
                out[cur_ind] = i - cur_ind
            stack.append([temperature, i])
        return out


        # [30,38,30,36,35,40,28]

        # [0, 0, 0, 0, 0, 0, 0]

        # []