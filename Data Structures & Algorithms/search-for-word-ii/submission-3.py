class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        # basically is a trienode, but can insert...
        for word in words:
            trie.add_word(word)

        ROWS = len(board)
        COLS = len(board[0])
        seen = set()
        res = set()

        def dfs(r, c, node, word):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in seen or board[r][c] not in node.children:
                return 

            # found a character in add
            seen.add((r, c)) # add to a set
            word += board[r][c] # build the word from '
            node = node.children[board[r][c]] # moving into the word

            if node.is_word:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            seen.remove((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, '')

        return list(res)
