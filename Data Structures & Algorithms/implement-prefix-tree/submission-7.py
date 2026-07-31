class TreeNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class PrefixTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root #?

        for char in word:
            # if not in, create a TreeNode there
            if char not in curr.children:
                curr.children[char] = TreeNode()

            # basically move inside
            curr = curr.children[char] #? feels wrong
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False

            curr = curr.children[char]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]

        return True