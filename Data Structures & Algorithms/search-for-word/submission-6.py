class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # name dimensions, rows, columns
        # we would have a simple dfs really, if board[r][c] == word[i]: dfs(i + 1), if i == len(word): return True, return False

        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(r, c, i):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != word[i] or (r, c) in visited:
                return False

            if i == len(word) - 1:
                return True

            visited.add((r, c))
            # we found a match, explore all 4 directions
            # the 4 directions pop up to us
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            visited.remove((r, c))
            return res

        i = 0

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[i]:
                    if dfs(r, c, i):
                        return True

        return False

