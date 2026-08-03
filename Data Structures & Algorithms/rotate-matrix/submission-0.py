class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # we set two pointers at L and R
        # we try to do a while loop of both terminals, 
        # and then do a for loop, n - 1 time and keeps decreasing
        l = 0
        r = len(matrix) - 1

        while l < r:
            for i in range(r - l):
                # save top left, move them in reverse order
                # topleft = bottomleft
                # bottomleft = bottomright
                # bottomright = topright
                # topright = saved
                top = l
                bottom = r

                saved_topLeft = matrix[top][l + i]

                # topleft = bottomleft
                matrix[top][l + i] = matrix[bottom - i][l]

                # bottomleft = bottomright
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # bottomright = topright
                matrix[bottom][r - i] = matrix[top + i][r]

                # topright = saved
                matrix[top + i][r] = saved_topLeft

            r -= 1
            l += 1

