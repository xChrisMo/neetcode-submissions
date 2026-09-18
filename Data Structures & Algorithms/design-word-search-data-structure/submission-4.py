class TreeNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TreeNode()

            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                char = word[i]
                # if word[i] == '.'
                # else it isnt i
                if char == '.':
                    for val in curr.children.values():
                        if dfs(i + 1, val) == True:
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.is_word

        return dfs(0, self.root)