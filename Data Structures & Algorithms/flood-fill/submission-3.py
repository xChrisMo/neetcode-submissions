from collections import deque 

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig_color = image[sr][sc]
        if orig_color == color:
            return image

        q = deque()

        ROWS = len(image)
        COLS = len(image[0])

        image[sr][sc] = color
        q.append([sr, sc])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == orig_color:
                        image[nr][nc] = color

                        q.append([nr, nc])

        
        return image