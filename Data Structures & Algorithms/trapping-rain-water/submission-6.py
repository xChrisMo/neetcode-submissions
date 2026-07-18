class Solution:
    def trap(self, height: List[int]) -> int:
        # i first want to use a o(n) memory technique where i precompute the max_value seen BOTH FROM THE LEFT and THE RIGHT

        n = len(height)

        # right_arr = [0] * n
        # max_r = 0
        # for i in range(n - 1, -1, -1):
        #     max_r = max(max_r, height[i])
        #     right_arr[i] = max_r


        # left_arr = [0] * n
        # max_l = 0
        # for i in range(n):
        #     max_l = max(max_l, height[i])
        #     left_arr[i] = max_l


        # print(left_arr)
        # print(right_arr)

        # res = 0

        # for i in range(n):
        #     res += min(right_arr[i], left_arr[i]) - height[i]

        # return res

        l = 0
        r = n - 1

        max_l = height[l]
        max_r = height[r]

        res = 0

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                res += max_l - height[l]

            else:
                r -= 1
                max_r = max(max_r, height[r])
                res += max_r - height[r]

        return res