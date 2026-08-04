class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_arr = [0] * n
        right_arr = [0] * n

        max_left = 0
        for i in range(n):
            left_arr[i] = max_left
            max_left = max(max_left, height[i])

        max_right = 0
        for i in range(n - 1, -1, -1):
            right_arr[i] = max_right
            max_right = max(max_right, height[i])

        print(left_arr)
        print(right_arr)
        
        res = 0

        for i in range(n):
            stored_water = min(left_arr[i], right_arr[i]) - height[i]
            res += stored_water if stored_water > 0 else 0

        return res