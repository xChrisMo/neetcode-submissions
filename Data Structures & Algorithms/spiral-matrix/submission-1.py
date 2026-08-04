class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # we want to point at the top, the bottom, the l, the r
        top = 0
        bottom = len(matrix)
        l = 0
        r = len(matrix[0])
        res = []

        while l < r and top < bottom:
            # we fill from l to r
            # we fill from r to bottom
            # we fill from bottomr to bottoml,
            # we fill from bottoml to topl

            # we fill from l to r
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1

            # we fill from r to bottom
            for i in range(top, bottom):
                res.append(matrix[i][r - 1])
            r -= 1

            if not (l < r and top < bottom):
                return res

            # we fill from bottomr to bottoml,
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # we fill from bottoml to topl
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res

