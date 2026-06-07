class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            #base case
            if i == len(word):
                return node.is_word


            #'.'
            char = word[i]
            if char == '.':
                for child in node.children.values():
                    if dfs(child, i + 1) == True:
                        return True

                return False

            else:
                if char not in node.children:
                    return False

                return dfs(node.children[char], i + 1)
                
        return dfs(self.root, 0)