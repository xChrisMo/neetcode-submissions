class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for every row, we want to check duplicates
        # for every column, we want to check duplicates
        # fpor every 3by3, we want to check duplicates

        # SOOO, we use a defaultdict(set), so if that set isnt created, it creates it and we move on!

        row_set = defaultdict(set)
        col_set = defaultdict(set)
        tri_set = defaultdict(set)

        # now we do double for loops to check really

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    #no need for this guy
                    continue


                else:
                    # check if it exists in all spaces
                    if board[r][c] in row_set[r] or board[r][c] in col_set[c] or board[r][c] in tri_set[(r // 3, c//3)]:
                        return False

                    tri_set[(r//3, c//3)].add(board[r][c])
                    col_set[c].add(board[r][c])
                    row_set[r].add(board[r][c])

        return True