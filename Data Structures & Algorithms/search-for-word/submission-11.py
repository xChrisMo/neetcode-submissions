class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        used = set()

        def dfs(r, c, i):
                
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != word[i] or (r, c) in used:
                return False

            if i == len(word) - 1:
                return True

            # found a match
            used.add((r, c))
            # make it unusable

            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            # backtrack
            used.remove((r, c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False
