class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, word: str) -> None:
        curr = self

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
        curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        
        root = TrieNode()
        
        for word in words:
            root.insert(word)

        visited = set()
        res = set()

        def dfs(r, c, node, word):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or board[r][c] not in node.children:
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_word == True:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            
            visited.remove((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, '')

        
        return list(res)