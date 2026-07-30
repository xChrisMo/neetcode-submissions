class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # for every letter, if letter in word, do a recursion on that
        # if we get to the end of the word, we return True...
        # if we dont, we return False


        # row
        # col
        
        # our dfs function
        # checks boundaries, checks nulls, checks if it mathces, if it does, we recursively run backtracking!
        # double for loop to call our dfs function

        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(i, r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i] or i > len(word) or (r, c) in visited:
                return False

            if i == len(word) - 1:
                return True

            visited.add((r, c))
            res = dfs(i + 1, r + 1, c) or dfs(i + 1, r - 1, c) or dfs(i + 1, r, c + 1) or dfs(i + 1, r, c - 1)
            visited.remove((r, c))
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(0, r, c):
                        return True

        return False