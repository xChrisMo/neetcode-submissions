class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # if it is a boundary shared, mark as T
        # mark all Os as Xs
        # mark all Ts as Os
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O':
                return 

            board[r][c] = 'T'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)


        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == 'O':
                    # mark it as 'T', go in its 4 directions
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                    # marking remaining Os as Xs


        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                    # marking remaining Os as Xs


        